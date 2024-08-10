import os
from pathlib import Path
from dotenv import load_dotenv
from core.utils.text_between_marks_parser import extract_enclosed_string
from core.res.result import Result
from  ..models.types import QuestionDetails,GeneratedResult
from core.requests.providers.groq import GroqPromptSender
from core.models.message import Message,MessageHistory,add_message_to_history
from core.regex.parser import parse_json




#########################################
## read the prompts files  🤖🤖🤖🤖  ##
#########################################

load_dotenv(override=True)
path = Path(__file__).parent.parent
task_path = os.path.join(path,"tasks/instructions/generate.prompt")
parser_path = os.path.join(path,"tasks/instructions/generate.format.prompt")

TASK_PROMPT = ""
FORMAT_PROMPT=""

with open(task_path, 'r') as file:
    TASK_PROMPT = file.read()

with open(parser_path, 'r') as file:
    FORMAT_PROMPT = file.read()
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

# the service class for this slice
class Service:
    def __init__(self):
        pass

    def serve(self, request : QuestionDetails):
        sender = GroqPromptSender()
        PROMPT = TASK_PROMPT
        if request.process_description != "":
            PROMPT = PROMPT + "\n**Process Description**:\n {process_description}"        
            PROMPT = PROMPT.replace("{process_description}",request.process_description)
        
        
        if request.report != "":
            PROMPT = PROMPT + "\n**Report**:\n {report}"        
            PROMPT = PROMPT.replace("{report}",request.report)
        
        if request.notes != "":
            PROMPT = PROMPT + "\n**Notes**:\n {notes}"        
            PROMPT = PROMPT.replace("{notes}",request.notes)
        
        llm_history = MessageHistory(messages=[
            Message(role="user",content=PROMPT)
        ])  
        
        llm_response = sender.send_prompt_history(llm_history)
        
        PROMPT = FORMAT_PROMPT.replace("{BPMN_Specification}",llm_response)
        
        llm_history = MessageHistory(messages=[
            Message(role="user",content=PROMPT)
        ])  
        
        llm_response = sender.send_prompt_history(llm_history)
        
       
        formating_result = parse_json(llm_response)

        if(formating_result.is_failure()):
            return Result.failure(formating_result.error)
        
        data = formating_result.value

        
                
        nodes = {}
        edges = []

        for actor, activities in data['actorActivityMapping'].items():
            nodes[actor] = {'name': actor, 'parentId': None,'type':"pool"}
            
            for activity in activities:
                if activity not in nodes:
                    nodes[activity] = {'name': activity, 'parentId': actor,'type':None}

        for process in data['process']:
            if process['from'] not in nodes:
                nodes[process['from']] = {'name': process['from'], 'parentId': None,'type':None}
            if process['to'] not in nodes:
                nodes[process['to']] = {'name': process['to'], 'parentId': None,'type':None}

       
            edge = {
                'from': process['from'],
                'to': process['to']
            }
            if 'condition' in process:
                edge['condition'] = process['condition']
            edges.append(edge)

        for element, type in data['elementTypeMapping'].items():
            if element in nodes:
                    nodes[element] = {'name': element, 'parentId': nodes[element]["parentId"],'type':type}
        

        nodes_list = [{'name': key, 'parentId': value['parentId'],'type': value['type']} for key, value in nodes.items()]

        
        
        return Result.success(GeneratedResult(nodes=nodes_list,
                                              edges=edges))