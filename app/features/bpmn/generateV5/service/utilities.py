def parse_flows(input_str):
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

def build_connections(activity_dict):
    connections = []

    for source, destinations in activity_dict.items():
        for destination in destinations:
            connections.append({"source":source,"target":destination})
    return connections
