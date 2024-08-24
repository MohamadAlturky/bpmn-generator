import json
from core.spec.model.task_spec import TaskSpecification


#############################################################
## Loads the task specification from some josn file.📂    ##
#############################################################

def load_task_specification(file_path) -> TaskSpecification:
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            task = TaskSpecification(**data)
        return task
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file at {file_path} is not a valid JSON file.")
    except TypeError as e:
        print(f"Error: Type mismatch when creating task object: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
