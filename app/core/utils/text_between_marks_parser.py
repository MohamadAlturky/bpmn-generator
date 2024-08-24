def extract_enclosed_string(input_string):
    print("extract_enclosed_string started")
    print(input_string)
    
    start_marker = "```"
    end_marker = "```"
    
    start_index = input_string.find(start_marker)
    end_index = input_string.find(end_marker, start_index + len(start_marker))
    
    print("start_index")
    print(start_index)
    print("end_index")
    print(end_index)
    if start_index != -1 and end_index != -1:
        enclosed_string = input_string[start_index + len(start_marker):end_index].strip()
        return enclosed_string
    else:
        return None
