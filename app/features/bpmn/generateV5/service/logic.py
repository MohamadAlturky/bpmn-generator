import json
import uuid
import os
from pathlib import Path
from dotenv import load_dotenv
from core.decorators.retry_policy import retry_on_exception
from core.factories.type import type_representer
from core.utils.text_between_marks_parser import extract_enclosed_string
from core.res.result import Result
from core.requests.providers.groq import GroqPromptSender
from core.models.message import Message,MessageHistory,add_message_to_history
from core.regex.parser import parse_json

from  ..models.types import QuestionDetails,GeneratedResult
from .utilities import parse_flows,build_connections,build_activity_dictionary

def find_edge(edges, source_value, target_value, condition):
    for edge in edges:
        if edge["source"] == source_value and edge["target"] == target_value:
            edge['condition'] = condition
            return edge
    return None


@retry_on_exception(max_retries=2, delay=2)
def get_elements_types(sender,llm_history):
    first_agent_message = sender.send_prompt_history(llm_history)
    
    print("get_elements_types get_elements_types get_elements_types get_elements_types")
    print(first_agent_message)
    
    formating_result = parse_json(first_agent_message)

    
    if(formating_result.is_failure()):
        raise TypeError("No flow provided")
    
    return formating_result.value


@retry_on_exception(max_retries=2, delay=2)
def get_flow(sender, llm_history):
    llm_response = sender.send_prompt_history(llm_history)
    print("the llm respondes with ")
    print(llm_response)
    input_str = extract_enclosed_string(llm_response)
    print("input_str")
    print(input_str)
    if input_str == None:
        raise TypeError("No flow provided")
    return input_str
    

#########################################
## read the prompts files  🤖🤖🤖🤖  ##
#########################################

load_dotenv(override=True)
path = Path(__file__).parent.parent
task_path = os.path.join(path,"tasks/instructions/generate.prompt")
parser_path = os.path.join(path,"tasks/instructions/types.extraction.prompt")
gateway_parser_path = os.path.join(path,"tasks/instructions/gateways.types.extraction.prompt")

TASK_PROMPT = ""
FORMAT_PROMPT=""
GATEWAYS_PROMPT=""

with open(task_path, 'r') as file:
    TASK_PROMPT = file.read()

with open(parser_path, 'r') as file:
    FORMAT_PROMPT = file.read()
    
with open(gateway_parser_path, 'r') as file:
    GATEWAYS_PROMPT = file.read()
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
        
        if request.notes != "":
            PROMPT = PROMPT + "\n**Notes**:\n {notes}"        
            PROMPT = PROMPT.replace("{notes}",request.notes)
        
        llm_history = MessageHistory(messages=[
            Message(role="user",content=PROMPT)
        ])  
        
        # @retry_on_exception(max_retries=5, delay=2)
        # def get_flow():
        #     llm_response = sender.send_prompt_history(llm_history)
        #     input_str = extract_enclosed_string(llm_response)
        #     if input_str == None:
        #         raise TypeError("No flow provided")
        
        input_str = get_flow(sender, llm_history)
        
        
        print("input_str input_str input_str input_str")
        print(input_str)
        
        parsed_workflows = parse_flows(input_str)
        
        print()
        print()
        print()
        print()
        print()
        for i in parsed_workflows:
            print(i)
        print()
        print()
        print()
        one_to_one_tree = build_activity_dictionary(parsed_workflows)
        new_tree = {}
        activities_set = set()
        activities_list = []
        gateways_list = []
        gateway = 1
        for source, destinations in one_to_one_tree.items():
            if len(destinations) > 1:
                new_tree[source] = [f"gateway {gateway}"]
                new_tree[f"gateway {gateway}"] = destinations
                gateways_list.append({
                    "name":f"gateway {gateway}",
                    "input activity":source,
                    "output activities":destinations,
                })
                gateway = gateway + 1
            
            elif len(destinations) == 1:
                new_tree[source] = destinations
            
            # building activities list 
            activities_set.add(source)
            for destination in destinations:
                activities_set.add(destination)
        
        activities_list = list(activities_set)
        connections = build_connections(new_tree)


        
        print("connections connections connections connections")
        print(connections)
        
        PROMPT = FORMAT_PROMPT.replace("{process_description}",request.process_description)
        PROMPT = PROMPT.replace("{BPMN_flows}", json.dumps(connections))
        PROMPT = PROMPT.replace("{activities}", json.dumps(activities_list))

        print("PROMPT PROMPT PROMPT PROMPT PROMPT PROMPT PROMPT")
        print(PROMPT)
        llm_history = MessageHistory(messages=[
            Message(role="user",content=PROMPT)
        ])  


        data = get_elements_types(sender,llm_history)
        
        
        
        
        print("data")
        print(data)
        
        
        
        
        
        # gateways section
        PROMPT = GATEWAYS_PROMPT.replace("{process_description}",request.process_description)
        PROMPT = PROMPT.replace("{gateways}", json.dumps(gateways_list))        
        
        print("PROMPT PROMPT PROMPT PROMPT PROMPT PROMPT PROMPT")
        print(PROMPT)
        llm_history = MessageHistory(messages=[
            Message(role="user",content=PROMPT)
        ])  
        
        first_agent_message = sender.send_prompt_history(llm_history)
    
        print("gatewaysgateways gateways gateways gateways gateways")
        print(first_agent_message)
        
        formating_result = parse_json(first_agent_message)

        
        if(formating_result.is_failure()):
            raise TypeError("No flow provided")
        
        print(formating_result.value)
    
        gateways_data = formating_result.value
        
        # 
        
        
        
        
        
        
        
        nodes = {}
        edges = []

        for actor, activities in data['actorActivityMapping'].items():
            nodes[actor] = {'id':uuid.uuid4(),'name': actor,'type':"pool"}
            # nodes[actor] = {'id':uuid.uuid4(),'name': actor, 'parentId': None,'type':"pool"}
            
            for activity in activities:
                if activity not in nodes:
                    nodes[activity] = {'id':uuid.uuid4(),'name': activity,'type':None}
                    # nodes[activity] = {'id':uuid.uuid4(),'name': activity, 'parentId': nodes[actor]['id'],'type':None}

        for process in connections:
            if process['source'] not in nodes:
                nodes[process['source']] = {'id':uuid.uuid4(),'name': process['source'], 'parentId': None,'type':None}
            if process['target'] not in nodes:
                nodes[process['target']] = {'id':uuid.uuid4(),'name': process['target'], 'parentId': None,'type':None}


            edge = {
                'id':uuid.uuid4(),
                'source': nodes[process['source']]['id'],
                'target': nodes[process['target']]['id']
            }
            # if 'condition' in process:
            #     edge['condition'] = process['condition']
            edges.append(edge)

        for element, type in data['elementTypeMapping'].items():
            if element in nodes:
                nodes[element] = {'id':nodes[element]["id"],'name': element,'type':type_representer(type)}
        for element, type in gateways_data['gatewayTypeMapping'].items():
            if element in nodes:
                nodes[element] = {'id':nodes[element]["id"],'name': element,'type':type_representer(type)}
                # nodes[element] = {'id':nodes[element]["id"],'name': element, 'parentId': nodes[element]["parentId"],'type':type_representer(type)}


        nodes_list = [{'id': value['id'],'name': key,'type': value['type']} for key, value in nodes.items()]
        # nodes_list = [{'id': value['id'],'name': key, 'parentId': value['parentId'],'type': value['type']} for key, value in nodes.items()]



        print()
        print()
        print()
        print()
        # Loop over the dictionary
        for gateway, activities in gateways_data["gatewayConditions"].items():
            print(f"Gateway: {gateway}")
            print(f"Gateway Node: {nodes[gateway]}")

            for activity, condition in activities.items():
                print(f"  Activity: {activity}")
                print(f"  Activity Node: {nodes[activity]}")
                find_edge(edges=edges,source_value=nodes[gateway]["id"],target_value=nodes[activity]["id"],condition=condition)
                print(f"    condition: {condition}")
        # print(nodes_list)
        # print(edges)
        return Result.success(GeneratedResult(nodes=nodes_list,
                                              edges=edges))