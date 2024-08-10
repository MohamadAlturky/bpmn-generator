import os
from pathlib import Path
from dotenv import load_dotenv
from core.res.result import Result
from  ..models.types import QuestionDetails,GeneratedResult
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
        if request.addtional_user_info != "":
            PROMPT = PROMPT + "\n" + "** Notes **" + "\n" + request.addtional_user_info
        print("PROMPT ======>>>>     \n",PROMPT)
        
        first_llm_history = MessageHistory(messages=[
            Message(role="user",content=PROMPT)
        ])  
        
        first_llm_response = sender.send_prompt_history(first_llm_history)
        print("first_llm_response-----------------------------------------------------------------")
        print(first_llm_response)
        
        add_message_to_history(first_llm_history, "assistant", first_llm_response)
        
        second_llm_history = MessageHistory(messages=[
            Message(
                role="assistant",
                content=PROMPT),
            Message(
                role="user",
                content=first_llm_response)
        ])
        
        
        for _ in range(request.number_of_iterations - 1):
            
            second_llm_response = sender.send_prompt_history(second_llm_history)
            print("second_llm_response-----------------------------------------------------------------")
            print(second_llm_response)
            
            add_message_to_history(second_llm_history,"assistant",second_llm_response)
            add_message_to_history(first_llm_history,"user",second_llm_response)
            
            first_llm_response = sender.send_prompt_history(first_llm_history)
            print("first_llm_response-----------------------------------------------------------------")
            print(first_llm_response)
            add_message_to_history(second_llm_history,"user",first_llm_response)
            add_message_to_history(first_llm_history,"assistant",first_llm_response)
        
        second_llm_response = sender.send_prompt_history(second_llm_history)
        second_llm_response = second_llm_response + FORMAT_PROMPT
        print("*********************************************************************")
        print("*********************************************************************")
        print("*********************************************************************")
        print("*********************************************************************")
        print(second_llm_response)
        add_message_to_history(first_llm_history,"user",second_llm_response)
        
        first_llm_response = sender.send_prompt_history(first_llm_history)
        
        add_message_to_history(first_llm_history,"assistant",first_llm_response)
        
        return Result.success(GeneratedResult(report=first_llm_history,
                                              edges="",
                                              nodes="",
                                              history=second_llm_history))