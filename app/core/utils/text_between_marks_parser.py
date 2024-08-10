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
