import os
import json
from pathlib import Path
import uuid
from dotenv import load_dotenv
from core.utils.text_between_marks_parser import extract_enclosed_string
from core.res.result import Result
from  ..models.types import QuestionDetails,GeneratedResult
from core.requests.providers.groq import GroqPromptSender
from core.models.message import Message,MessageHistory,add_message_to_history


# utils

def process_json_data(types, connections, parent):    
    nodes = []
    edges = []
    node_ids = {}  
    parentId =  str(uuid.uuid4())
    nodes.append({"id":  parentId , "name": parent, "type":"type","type_name": "relation","parentId":None})

    node_types = types

    for entry in connections:
        source = entry[0]  
        condition = entry[1]  
        target = entry[2]  
        
        if source not in node_ids:
            node_id = str(uuid.uuid4())  
            node_ids[source] = node_id
            nodes.append({"id": node_id, "name": source, "type":"type","type_name": node_types.get(source, "not specified"),"parentId":parentId})

        if target not in node_ids:
            node_id = str(uuid.uuid4())  
            node_ids[target] = node_id
            nodes.append({"id": node_id, "name": target, "type":"type","type_name": node_types.get(target, "not specified"),"parentId":parentId})

        edges.append({
            "id": str(uuid.uuid4()),
            "source": node_ids[source],
            "target": node_ids[target],
            "condition": condition
        })

    return {"nodes": nodes, "edges": edges}


def group_by_connection(data):
    result = {}
    
    for item in data:
        middle = item[1]
        if middle not in result:
            result[middle] = []
        result[middle].append(item)
    
    return result


def flatten(objects):

    flattened_nodes = []
    flattened_edges = []

    for obj in objects:
        flattened_nodes.extend(obj.get('nodes', []))
        flattened_edges.extend(obj.get('edges', []))

    return flattened_nodes, flattened_edges

#########################################
## read the prompts files  🤖🤖🤖🤖  ##
#########################################

load_dotenv(override=True)
path = Path(__file__).parent.parent
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

# the service class for this slice
class Service:
    def __init__(self):
        pass

    def serve(self, request : QuestionDetails):
        path = Path(__file__).parent.parent
        parser_path = os.path.join(path,f"tasks/{request.row_num}/result_row.json")
        content = ""
        with open(parser_path, 'r') as file:
            content = file.read()
            # print(content)
        try:
            parsed_content = json.loads(content)
            print(parsed_content)
        except json.JSONDecodeError as e:
            return Result.failure(f"Error parsing JSON: {str(e)}")
        
        results = []
        for middle_element, items in group_by_connection(parsed_content['answer']).items():
            results.append(process_json_data(parsed_content['types'],items,middle_element))
        
        nodes,edges = flatten(results)
        # processed_json_data = process_json_data(parsed_content['types'],parsed_content['answer'])
        return Result.success(GeneratedResult(edges=edges,nodes=nodes))