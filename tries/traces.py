import json
import re
import uuid
from groq import Groq


def extract_enclosed_string(input_string):
    
    start_marker = "```"
    end_marker = "```"
    
    start_index = input_string.find(start_marker)
    end_index = input_string.find(end_marker, start_index + len(start_marker))
    
    if start_index != -1 and end_index != -1:
        enclosed_string = input_string[start_index + len(start_marker):end_index].strip()
        return enclosed_string
    else:
        return None


client = Groq(
    api_key="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"
)

process_description = "Consider a process for purchasing items from an online shop. The user starts an order by logging in to their account. Then, the user simultaneously selects the items to purchase and sets a payment method. Afterward, the user either pays or completes an installment agreement. Since the reward value depends on the purchase value, After selecting the items, the user chooses between multiple options for a free reward. this step is done after selecting the items, but it is independent of the payment activities. Finally, the items are delivered. The user has the right to return items for exchange. Every time items are returned, a new delivery is made."

initial_prompt = {
    "role": "user",
    "content": f"""
                Generate all possible sequences of activities for the provided Process Description
                
                **Process Description**:
                {process_description}
                
                Expected Output Example:
                ```
                    Activity1 -> Activity2 -> Activity3
                    Activity1 -> Activity4 -> Activity5
                ```

                Apply this logic to the process description provided to generate all potential sequences and return the result between this markers ``` ```. Follow the instructions given and do not add any additional information.
                """
}

def send_message(messages, model="llama-3.1-70b-versatile"):
    response = client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return response.choices[0].message.content

first_agent_message = send_message([initial_prompt])

def parse_workflow(input_str):
    # Split the input by newlines to process each workflow separately
    lines = input_str.strip().split('\n')
    
    # Initialize an empty list to store the parsed workflows
    workflows = []
    
    # Process each line
    for line in lines:
        # Split each line by '->' and remove extra spaces
        steps = [step.strip() for step in line.split('->')]
        workflows.append(steps)
    
    return workflows




print(first_agent_message)
print("------------------")
print("------------------")
print("------------------")
print("------------------")
print("------------------")
input_str = extract_enclosed_string(first_agent_message)
print(input_str)
if input_str == None:
    raise TypeError("")
parsed_workflows = parse_workflow(input_str)

print("")

# Output the parsed list of lists
for workflow in parsed_workflows:
    print(workflow)



def build_tree(parsed_workflows):
    tree = {}
    
    # Iterate through each workflow
    for workflow in parsed_workflows:
        current_node = tree
        
        for step in workflow:
            if step not in current_node:
                current_node[step] = {}
            current_node = current_node[step]
    
    return tree







def build_tree_with_gateway(parsed_workflows):
    id = 1
    # Initialize the root of the tree
    tree = {}
    
    # Iterate through each workflow
    for workflow in parsed_workflows:
        current_node = tree
        
        # Traverse the workflow steps
        for step in workflow:
            if step not in current_node:
                current_node[step] = {}
            current_node = current_node[step]
            
            # Check if the current node has more than one child
            if len(current_node) > 1:
                # Move the existing children to a "gateway" node
                gateway_node = {f'gateway {id}': current_node.copy()}
                # Clear the current node and replace it with the "gateway" node
                current_node.clear()
                current_node.update(gateway_node)
                # Move to the "gateway" node for the next step
                current_node = current_node[f'gateway {id}']
                id = id + 1
    
    return tree



# Output the tree with gateways

workflow_tree_with_gateway = build_tree_with_gateway(parsed_workflows)

# Output the tree
# import pprint
# print()
# pprint.pprint(workflow_tree_with_gateway)

connections = []
def traverse_tree_with_parents(tree, parent=None):
    for key, value in tree.items():
        # Print the current element with its parent
        # print(f"Element: {key}, Parent: {parent}")
        if parent != None:
            connections.append({"source":parent,"target":key})
        # If the current element has children, recursively call the function
        if isinstance(value, dict):
            traverse_tree_with_parents(value, parent=key)
            
traverse_tree_with_parents(workflow_tree_with_gateway)
print()
print()
print()

for i in connections:
    print(i)

    
PROMPT = """
given the following process description flows:

**Process Description**:
{process_description}

given the following BPMN flows:
**BPMN flow**:
{BPMN_flows}

provide the "actorActivityMapping" object that maps each actor to their respective activities and the "elementTypeMapping" that maps each element to a type.

**Expected JSON Format**:

```json
{
  "actorActivityMapping": {
    "Actor1": [
      "Activity 1",
      "Activity 2",
    ],
    "Actor2": [
      "Activity 8",
      "Activity 9"
    ]
  },
  "elementTypeMapping":{
    "some activity 3":"user task",
    "some activity 2":"manual task",
    "some activity 1":"system task",
    "some gateway":"xor gateway",
    "Start":"start event"
  }
}
```


in the elementTypeMapping the types are:
- "user task"
- "service task"
- "manual task"
- "and gateway"
- "xor gateway"
- "or gateway"
- "start event"
- "intermediate event"
- "end event"
- "pool"

don't specify any type other than the provided list.

Please ensure the JSON structure accurately reflects the BPMN specification provided.
"""

PROMPT = PROMPT.replace("{process_description}",process_description)
PROMPT = PROMPT.replace("{BPMN_flows}", json.dumps(connections))






initial_prompt = {
    "role": "user",
    "content": PROMPT
}

first_agent_message = send_message([initial_prompt])
print()
print()
print()
print()
print(first_agent_message)


# 
# 
# 
# 



def parse_json(input_string):
    
    start_marker = "``` json"
    end_marker = "```"

    match = re.search(f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", input_string, re.DOTALL)
    if match:
        json_content = match.group(1)
        # print("-------------------------------------------------------------------------------------------")
        # print(json_content)
        # print("-------------------------------------------------------------------------------------------")
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
        # print("-------------------------------------------------------------------------------------------")
        # print(json_content)
        # print("-------------------------------------------------------------------------------------------")
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
        # print("-------------------------------------------------------------------------------------------")
        # print(json_content)
        # print("-------------------------------------------------------------------------------------------")
        try:
            parsed_json = json.loads(json_content)
            # print(parsed_json)
            return parsed_json
        except json.JSONDecodeError:
            raise TypeError()
    else:
        raise TypeError()








# /
# 
# 
# /


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



formating_result = parse_json(first_agent_message)


data = formating_result

print("data")
print(data)
print()
print()
print()
print()
print()
print()



nodes = {}
edges = []

for actor, activities in data['actorActivityMapping'].items():
    nodes[actor] = {'id':uuid.uuid4(),'name': actor, 'parentId': None,'type':"pool"}
    
    for activity in activities:
        if activity not in nodes:
            nodes[activity] = {'id':uuid.uuid4(),'name': activity, 'parentId': nodes[actor]['id'],'type':None}

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
    if 'condition' in process:
        edge['condition'] = process['condition']
    edges.append(edge)

for element, type in data['elementTypeMapping'].items():
    if element in nodes:
            nodes[element] = {'id':nodes[element]["id"],'name': element, 'parentId': nodes[element]["parentId"],'type':type_representer(type)}


nodes_list = [{'id': value['id'],'name': key, 'parentId': value['parentId'],'type': value['type']} for key, value in nodes.items()]

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print("nodes_list")
print(nodes_list)
print()
print()
print()
print()
print()
print() 
print()
print()
print()
print("edges")
print(edges)
print()
print()
print()
print()
print()
