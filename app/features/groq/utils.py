
def convert_bpmn_to_nodes_and_edges(bpmn_json):
    # data = json.loads(bpmn_json)
    elements = bpmn_json['elements']

    nodes = []
    edges = []
    
    # Constants for node layout
    node_width = 100
    node_height = 50
    horizontal_spacing = 150
    vertical_spacing = 100
    nodes_per_row = 5

    # Helper function to get node by id
    def get_node_by_id(node_id):
        return next((node for node in nodes if node['id'] == node_id), None)

    # Create nodes
    for i, element in enumerate(elements):
        if element['type'] != 'SequenceFlow':
            row = i // nodes_per_row
            col = i % nodes_per_row
            node = {
                'id': element['id'],
                'type': element['type'],
                'data': {"label":element['name']+ " " + element['type']},
                'position':{
                        'x': col * (node_width + horizontal_spacing),
                        'y': row * (node_height + vertical_spacing)
                }
            }
            nodes.append(node)

    # Create edges
    for element in elements:
        if element['type'] == 'SequenceFlow':
            source = get_node_by_id(element['sourceRef'])
            target = get_node_by_id(element['targetRef'])
            if source and target:
                edge = {
                    'id':element['sourceRef'] +"_"+ element['targetRef'],
                    'source': element['sourceRef'],
                    'target': element['targetRef'],
                    'animated':True
                }
                edges.append(edge)

    return nodes, edges

import re
import json

def parse_json(input_string):
    
    start_marker = "``` json"
    end_marker = "```"

    match = re.search(f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", input_string, re.DOTALL)
    if match:
        json_content = match.group(1)
        print("-------------------------------------------------------------------------------------------")
        print(json_content)
        print("-------------------------------------------------------------------------------------------")
        try:
            parsed_json = json.loads(json_content)
            # print(parsed_json)
            return parsed_json
        except json.JSONDecodeError:
            pass
            # return Result.failure("Invalid JSON format.")
    else:
        pass
        # return Result.failure("No JSON content found.")


    start_marker = "```json"
    end_marker = "```"

    match = re.search(f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", input_string, re.DOTALL)
    if match:
        json_content = match.group(1)
        print("-------------------------------------------------------------------------------------------")
        print(json_content)
        print("-------------------------------------------------------------------------------------------")
        try:
            parsed_json = json.loads(json_content)
            # print(parsed_json)
            return parsed_json
        except json.JSONDecodeError:
            pass
            # return Result.failure("Invalid JSON format.")
    else:
        pass
        # return Result.failure("No JSON content found.")


    start_marker = "```"
    end_marker = "```"

    match = re.search(f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", input_string, re.DOTALL)
    if match:
        json_content = match.group(1)
        print("-------------------------------------------------------------------------------------------")
        print(json_content)
        print("-------------------------------------------------------------------------------------------")
        try:
            parsed_json = json.loads(json_content)
            # print(parsed_json)
            return parsed_json
        except json.JSONDecodeError:
            return "Invalid JSON format."
    else:
        return "No JSON content found."
