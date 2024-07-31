import os
from core.spec.json.task_reader import load_task_specification


cash = {}
class SpecificationRegistry:
    
    @staticmethod
    def get_specification(path):

        if path in cash.keys():
            print("return from cash !!!")
            return cash[path]
        
        tasks_path = os.path.join(os.getcwd(), "src\\tasks")
        print(tasks_path)
        
        file_path = os.path.join(tasks_path, path)
        print(file_path)
        cash[path] = load_task_specification(file_path)
        return cash[path]