#########################################
## import libraries 📕📗📘📙📔📗📘📒📚##
#########################################

##🔗 from python
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from pathlib import Path

##🔗 from application core
from core.res.result import Result
from core.regex.parser import parse_json

##🔗 from the same slice
from  ..models.types import ProcessDescription,EventsReport
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#



#########################################
## read the prompts files  🤖🤖🤖🤖  ##
#########################################

load_dotenv(override=True)
path = Path(__file__).parent.parent
task_path = os.path.join(path,"tasks/events/generate.prompt")
parser_path = os.path.join(path,"tasks/events/generate.format.prompt")

TASK_PROMPT = ""
FORMAT_PROMPT=""

with open(task_path, 'r') as file:
    TASK_PROMPT = file.read()

with open(parser_path, 'r') as file:
    FORMAT_PROMPT = file.read()
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


def generate_events_report(process_description : ProcessDescription):        
    
    PROMPT = TASK_PROMPT
    llm = Ollama(model="llama3.1", base_url=os.getenv("OLLAMA_HOST"))
    complete_prompt = PROMPT.replace("{process_description}", process_description.content)
    generated = llm.invoke(complete_prompt)
    
    PROMPT = FORMAT_PROMPT
    llm = Ollama(model="llama3.1", base_url=os.getenv("OLLAMA_HOST"))
    complete_prompt = PROMPT.replace("{events}", generated)
    generated_json = llm.invoke(complete_prompt)
    print("generate_events_report", generated_json)
    json_res = parse_json(generated_json)
    if json_res.is_failure:
        return json_res
    return Result.success(EventsReport(content=json_res.value))
