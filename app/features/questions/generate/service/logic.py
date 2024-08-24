import os
from pathlib import Path
from dotenv import load_dotenv
from core.regex.parser import parse_json
from core.utils.text_between_marks_parser import extract_enclosed_string
from core.res.result import Result
from  ..models.types import QuestionDetails,GeneratedResult,Question
from core.requests.providers.groq import GroqPromptSender
from core.models.message import Message,MessageHistory,add_message_to_history




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
        PROMPT = TASK_PROMPT.replace("{process_description}",request.process_description)
        
        llm_history = MessageHistory(messages=[
            Message(role="user",content=PROMPT)
        ])  
        
        llm_response = sender.send_prompt_history(llm_history)
        
        prompt = FORMAT_PROMPT.replace("{llm_response}",llm_response)
        llm_history = MessageHistory(messages=[
            Message(role="user",content=prompt)
        ])  
        llm_response = sender.send_prompt_history(llm_history)
        
        questions_result = parse_json(llm_response)
        print(questions_result.value)
        if(questions_result.is_failure()):
            return Result.failure(questions_result.error)
        
        questions=[]
        print(questions_result.value)
        for i in questions_result.value:
            questions.append(Question(question=i["question"]))
        print(questions)
        return Result.success(GeneratedResult(questions=questions))