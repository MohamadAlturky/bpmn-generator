import json
import uuid

def process_json_data(json_data):

    parsed_data = json.loads(json_data)
    
    
    nodes = []
    edges = []
    node_ids = {}  

    
    node_types = parsed_data['types']

    
    for entry in parsed_data['answer']:
        source = entry[0]  
        condition = entry[1]  
        target = entry[2]  

        
        if source not in node_ids:
            node_id = str(uuid.uuid4())  
            node_ids[source] = node_id
            nodes.append({"id": node_id, "name": source, "type":"type","type_name": node_types[source]})

        
        if target not in node_ids:
            node_id = str(uuid.uuid4())  
            node_ids[target] = node_id
            nodes.append({"id": node_id, "name": target, "type":"type","type_name": node_types[target]})

        
        edges.append({
            "id": str(uuid.uuid4()),
            "source": node_ids[source],
            "target": node_ids[target],
            "condition": condition
        })

    return {"nodes": nodes, "edges": edges}

json_input = '''{
    "types": {
        "the sales department": "Actor", 
        "receives": "Activity",
        "an order": "Activity Data",
        "reject": "Activity",
        "or": "XOR Gateway",
        "accept": "Activity",
        "the order": "Activity Data",
        "the storehouse": "Actor",
        "the engineering department": "Actor",
        "informed": "Activity",
        "The storehouse": "Actor",
        "processes": "Activity",
        "the part list of the order": "Activity Data",
        "checks": "Activity",
        "the required quantity of each part": "Activity Data",
        "If": "XOR Gateway",
        "the part is available in-house": "Condition Specification",
        "it": "Activity Data",
        "reserved": "Activity",
        "it is not available": "Condition Specification",
        "back-ordered": "Activity",
        "In the meantime": "AND Gateway",
        "prepares": "Activity",
        "everything": "Activity Data",
        "the storehouse has successfully reserved or back-ordered every item of the part list": "Condition Specification",
        "assembles": "Activity",
        "the bicycle": "Activity Data",
        "ships": "Activity",
        "the customer": "Actor"
    },
    "answer": [
        ["receives", "uses", "an order"],
        ["receives", "flow", "or"],
        ["receives", "actor recipient", "the sales department"],
        ["reject", "uses", "the order"],
        ["or", "flow", "reject"],
        ["or", "flow", "accept"],
        ["accept", "uses", "the order"],
        ["accept", "flow", "informed"],
        ["informed", "actor recipient", "the storehouse"],
        ["informed", "flow", "In the meantime"],
        ["informed", "actor recipient", "the engineering department"],
        ["processes", "uses", "the part list of the order"],
        ["processes", "actor performer", "The storehouse"],
        ["processes", "flow", "checks"],
        ["checks", "uses", "the required quantity of each part"],
        ["checks", "actor performer", "The storehouse"],
        ["checks", "flow", "If"],
        ["If", "flow", "the part is available in-house"],
        ["If", "same gateway", "If"],
        ["the part is available in-house", "flow", "reserved"],
        ["reserved", "uses", "it"],
        ["reserved", "flow", "If"],
        ["If", "flow", "it is not available"],
        ["it is not available", "flow", "back-ordered"],
        ["back-ordered", "uses", "it"],
        ["back-ordered", "flow", "If"],
        ["In the meantime", "flow", "prepares"],
        ["In the meantime", "flow", "processes"],
        ["prepares", "actor performer", "the engineering department"],
        ["prepares", "uses", "everything"],
        ["prepares", "flow", "If"],
        ["If", "flow", "the storehouse has successfully reserved or back-ordered every item of the part list"],
        ["the storehouse has successfully reserved or back-ordered every item of the part list", "flow", "assembles"],
        ["assembles", "uses", "the bicycle"],
        ["assembles", "actor performer", "the engineering department"],
        ["assembles", "flow", "ships"],
        ["ships", "uses", "the bicycle"],
        ["ships", "actor recipient", "the customer"],
        ["ships", "actor performer", "the sales department"]
    ]
}'''

result = process_json_data(json_input)
print(json.dumps(result, indent=4))