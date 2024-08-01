import re
import json
from core.res.result import Result

def parse_json(input_string):
    
    start_marker = "```json"
    end_marker = "```"

    match = re.search(f"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", input_string, re.DOTALL)
    if match:
        json_content = match.group(1)
        try:
            parsed_json = json.loads(json_content)
            # print(parsed_json)
            return Result.success(parsed_json)
        except json.JSONDecodeError:
            return Result.failure("Invalid JSON format.")
    else:
        return Result.failure("No JSON content found.")
