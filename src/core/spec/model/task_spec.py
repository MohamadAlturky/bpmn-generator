from pydantic import BaseModel

class TaskSpecification(BaseModel):
    role:str
    goal:str
    backstory:str
    description:str
    expected_output:str
