# import json

# # Sample traces
# traces = [
#     ["Login", "Select Items", "Set Payment Method", "Pay"],
#     ["Login", "Select Items", "Set Payment Method", "Installment Agreement"],
#     ["Login", "Select Items", "Choose Reward", "Set Payment Method", "Pay"],
#     ["Login", "Select Items", "Choose Reward", "Set Payment Method", "Installment Agreement"],
#     ["Login", "Select Items", "Set Payment Method", "Return Items", "Deliver Items"],
#     ["Login", "Select Items", "Return Items", "Deliver Items"]
# ]

# def generate_bpmn_json(traces):
#     # Create a set of unique activities
#     activities = set()
#     for trace in traces:
#         activities.update(trace)
    
#     # Map activities to unique IDs
#     activity_id_map = {activity: f"Activity_{i+1}" for i, activity in enumerate(activities)}
    
#     # Create BPMN elements
#     nodes = []
#     edges = []
    
#     for trace in traces:
#         for i in range(len(trace) - 1):
#             source = activity_id_map[trace[i]]
#             target = activity_id_map[trace[i + 1]]
#             edges.append({
#                 "source": source,
#                 "target": target
#             })
        
#         # Add nodes
#         for activity, activity_id in activity_id_map.items():
#             nodes.append({
#                 "id": activity_id,
#                 "name": activity
#             })
    
#     # Create BPMN JSON
#     bpmn_json = {
#         "nodes": nodes,
#         "edges": edges
#     }
    
#     return json.dumps(bpmn_json, indent=4)

# # Generate BPMN JSON
# bpmn_json = generate_bpmn_json(traces)

# # Print BPMN JSON
# print(bpmn_json)




import json

# Sample traces
traces = [
    ["Login", "Select Items", "Set Payment Method", "Pay"],
    ["Login", "Select Items", "Set Payment Method", "Installment Agreement"],
    ["Login", "Select Items", "Choose Reward", "Set Payment Method", "Pay"],
    ["Login", "Select Items", "Choose Reward", "Set Payment Method", "Installment Agreement"],
    ["Login", "Select Items", "Set Payment Method", "Return Items", "Deliver Items"],
    ["Login", "Select Items", "Return Items", "Deliver Items"]
]

def generate_bpmn_json(traces):
    # Create a set of unique activities and identify start and end events
    activities = set()
    start_events = set()
    end_events = set()
    
    for trace in traces:
        activities.update(trace)
        start_events.add(trace[0])
        end_events.add(trace[-1])
    
    # Map activities to unique IDs
    activity_id_map = {activity: f"Activity_{i+1}" for i, activity in enumerate(activities)}
    gateway_id = "Gateway_1"

    # Create BPMN elements
    nodes = []
    edges = []
    
    # Add start events
    for event in start_events:
        nodes.append({
            "id": f"StartEvent_{activity_id_map[event]}",
            "name": f"Start: {event}",
            "type": "startEvent"
        })

    # Add activities and end events
    for activity, activity_id in activity_id_map.items():
        nodes.append({
            "id": activity_id,
            "name": activity,
            "type": "activity"
        })
    
    for event in end_events:
        nodes.append({
            "id": f"EndEvent_{activity_id_map[event]}",
            "name": f"End: {event}",
            "type": "endEvent"
        })
    
    # Add a gateway
    nodes.append({
        "id": gateway_id,
        "name": "Decision Point",
        "type": "gateway"
    })

    for trace in traces:
        for i in range(len(trace) - 1):
            source = activity_id_map[trace[i]]
            target = activity_id_map[trace[i + 1]]
            edges.append({
                "source": source,
                "target": target
            })

        # Add transitions between start events and the first activity
        start_event_id = f"StartEvent_{activity_id_map[trace[0]]}"
        first_activity_id = activity_id_map[trace[1]]
        edges.append({
            "source": start_event_id,
            "target": first_activity_id
        })

        # Add transitions between activities and the gateway (if applicable)
        for i in range(len(trace) - 1):
            if i == len(trace) - 2:
                last_activity_id = activity_id_map[trace[i]]
                end_event_id = f"EndEvent_{activity_id_map[trace[i + 1]]}"
                edges.append({
                    "source": last_activity_id,
                    "target": end_event_id
                })
            else:
                source = activity_id_map[trace[i]]
                target = activity_id_map[trace[i + 1]]
                edges.append({
                    "source": source,
                    "target": target
                })

    # Create BPMN JSON
    bpmn_json = {
        "nodes": nodes,
        "edges": edges
    }
    
    return json.dumps(bpmn_json, indent=4)

# Generate BPMN JSON
bpmn_json = generate_bpmn_json(traces)

# Print BPMN JSON
print(bpmn_json)
