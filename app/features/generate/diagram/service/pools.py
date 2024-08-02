#########################################
## import libraries 📕📗📘📙📔📗📘📒📚##
#########################################

##🔗 from python
import os
import json
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from pathlib import Path

##🔗 from application core
from core.res.result import Result
from core.regex.parser import parse_json

##🔗 from the same slice
from  ..models.types import ProcessReport,Connections,Annotations
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#



#########################################
## read the prompts files  🤖🤖🤖🤖  ##
#########################################

load_dotenv(override=True)
path = Path(__file__).parent.parent
task_path = os.path.join(path,"tasks/pools/generate.prompt")
parser_path = os.path.join(path,"tasks/pools/generate.format.prompt")

TASK_PROMPT = ""
FORMAT_PROMPT=""

with open(task_path, 'r') as file:
    TASK_PROMPT = file.read()

with open(parser_path, 'r') as file:
    FORMAT_PROMPT = file.read()
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


def generate_annotations_report(process_report : ProcessReport,connections : Connections):        
    
    
    names = set()

    for item in connections.connections:
        names.add(item["source name"])
        names.add(item["destination name"])

    bpmn_components = ""
    for name in sorted(names):
        bpmn_components = bpmn_components + name + "\n"

    
    
    
    PROMPT = TASK_PROMPT
    llm = Ollama(model="llama3.1", base_url=os.getenv("OLLAMA_HOST"))
    complete_prompt = PROMPT.replace("{process_description}", process_report.content)
    complete_prompt = complete_prompt.replace("{bpmn_components}", bpmn_components)
    complete_prompt = complete_prompt.replace("{extracted_pools_and_lanes}", json.dumps(process_report.report.poolsLanes_report.content))
    generated = llm.invoke(complete_prompt)
    
    PROMPT = FORMAT_PROMPT
    llm = Ollama(model="llama3.1", base_url=os.getenv("OLLAMA_HOST"))
    complete_prompt = PROMPT.replace("{annotations}", generated)
    generated_json = llm.invoke(complete_prompt)
    print("generate_connections_report", generated_json)

    json_res = parse_json(generated_json)
    if json_res.is_failure:
        return json_res
    return Result.success(Annotations(annotations=json_res.value))
