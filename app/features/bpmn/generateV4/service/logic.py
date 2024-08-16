import json
import uuid
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


def type_representer(type):
    if type == "pool":
        return "pool"
    
    if type == "end event":
        return "End_Event"
    if type == "intermediate event":
        return "Intermediate_Event"
    if type == "start event":
        return "Start_Event"
    
    if type == "or gateway":
        return "OR"
    if type == "xor gateway":
        return "XOR"
    if type == "and gateway":
        return "AND"
    
    if type == "manual task":
        return "ManualTask"
    if type == "service task":
        return "ServiceTask"
    if type == "user task":
        return "UserTask"
    return type

def parse_workflow(input_str):
    lines = input_str.strip().split('\n')
    
    workflows = []
    
    for line in lines:
        steps = [step.strip() for step in line.split('->')]
        workflows.append(steps)
    
    return workflows



def build_activity_dictionary(activity_lists):
    activity_dict = {}

    for activity_list in activity_lists:
        for i in range(len(activity_list) - 1):
            source = activity_list[i]
            destination = activity_list[i + 1]

            if source not in activity_dict:
                activity_dict[source] = []

            if destination not in activity_dict[source]:
                activity_dict[source].append(destination)

    return activity_dict

# def build_tree_with_gateway(parsed_workflows):
#     id = 1
#     # Initialize the root of the tree
#     tree = {}
    
#     # Iterate through each workflow
#     for workflow in parsed_workflows:
#         current_node = tree
        
#         # Traverse the workflow steps
#         for step in workflow:
#             if step not in current_node:
#                 current_node[step] = {}
#             current_node = current_node[step]
            
#             # Check if the current node has more than one child
#             if len(current_node) > 1:
#                 # Move the existing children to a "gateway" node
#                 gateway_node = {f'gateway {id}': current_node.copy()}
#                 # Clear the current node and replace it with the "gateway" node
#                 current_node.clear()
#                 current_node.update(gateway_node)
#                 # Move to the "gateway" node for the next step
#                 current_node = current_node[f'gateway {id}']
#                 id = id + 1
    
#     return tree


# def build_tree(traces):
#     tree = {}

#     for trace in traces:
#         current_level = tree
#         for action in trace:
#             if action not in current_level:
#                 current_level[action] = {}
#             current_level = current_level[action]
    
#     return tree

# def build_tree(paths):
#     tree = {}

#     for path in paths:
#         current_level = tree
#         for step in path:
#             if step not in current_level:
#                 current_level[step] = {}
#             current_level = current_level[step]
    
#     return tree

# def build_tree_with_gateway(paths):
#     tree = {}
#     gateway_counter = 1

#     def add_gateway_node(node):
#         nonlocal gateway_counter
#         if len(node) > 1:
#             gateway_key = f"Gateway {gateway_counter}"
#             gateway_counter += 1
#             # Move all children to the gateway node
#             node[gateway_key] = {k: node[k] for k in list(node.keys())}
#             # Clear the original node children
#             for key in list(node.keys()):
#                 if key != gateway_key:
#                     del node[key]
#             return node[gateway_key]
#         return node

#     for path in paths:
#         current_level = tree
#         for step in path:
#             if step not in current_level:
#                 current_level[step] = {}
#             current_level = current_level[step]
#         # After inserting the entire path, check if the current node needs a gateway
#         add_gateway_node(current_level)
    
#     return tree
def build_connections(activity_dict):
    connections = []

    for source, destinations in activity_dict.items():
        for destination in destinations:
            connections.append({"source":source,"target":destination})
            # connections.append((source, destination))

    return connections


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
        
        llm_response = sender.send_prompt_history(llm_history)
        
        print("llm_responsellm_responsellm_responsellm_responsellm_responsellm_response")
        print(llm_response)
        
        input_str = extract_enclosed_string(llm_response)
        print("input_strinput_strinput_strinput_strinput_strinput_strinput_strinput_strinput_str")
        print(input_str)
        if input_str == None:
            raise TypeError("")
        parsed_workflows = parse_workflow(input_str)
        
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
        gateway = 1
        for source, destinations in one_to_one_tree.items():
            if len(destinations) > 1:
                new_tree[source] = [f"gateway {gateway}"]
                new_tree[f"gateway {gateway}"] = destinations
                gateway = gateway + 1
            elif len(destinations) == 1:
                new_tree[source] = destinations
                
        
        print(one_to_one_tree)
        print("workflow_tree_with_gatewayworkflow_tree_with_gatewayworkflow_tree_with_gatewayworkflow_tree_with_gateway")
        print(one_to_one_tree)
        
        
        connections = build_connections(new_tree)
        # def traverse_tree_with_parents(tree, parent=None):
        #     for key, value in tree.items():
        #         # Print the current element with its parent
        #         # print(f"Element: {key}, Parent: {parent}")
        #         if parent != None:
        #             connections.append({"source":parent,"target":key})
        #         # If the current element has children, recursively call the function
        #         if isinstance(value, dict):
        #             traverse_tree_with_parents(value, parent=key)
                    
        # traverse_tree_with_parents(workflow_tree_with_gateway)

        
        
        print("connectionsconnectionsconnectionsconnectionsconnectionsconnections")
        print(connections)
        
        PROMPT = FORMAT_PROMPT.replace("{process_description}",request.process_description)
        PROMPT = PROMPT.replace("{BPMN_flows}", json.dumps(connections))


        llm_history = MessageHistory(messages=[
            Message(role="user",content=PROMPT)
        ])  

        first_agent_message = sender.send_prompt_history(llm_history)
        
        print("first_agent_messagefirst_agent_messagefirst_agent_messagefirst_agent_message")
        print(first_agent_message)
        
        formating_result = parse_json(first_agent_message)

        
        if(formating_result.is_failure()):
            return Result.failure(formating_result.error)
        
        data = formating_result.value

                
                
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
                # nodes[element] = {'id':nodes[element]["id"],'name': element, 'parentId': nodes[element]["parentId"],'type':type_representer(type)}


        nodes_list = [{'id': value['id'],'name': key,'type': value['type']} for key, value in nodes.items()]
        # nodes_list = [{'id': value['id'],'name': key, 'parentId': value['parentId'],'type': value['type']} for key, value in nodes.items()]

        # print(nodes_list)
        # print(edges)
        return Result.success(GeneratedResult(nodes=nodes_list,
                                              edges=edges))