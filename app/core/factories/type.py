
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