from pydantic import BaseModel

#############################################################
## Contains the task definition to give it to an agent. 🤖 ##
#############################################################
## ROLE: The Agent Role.🧘🏼                                 ##
#############################################################
## GOAL: What We Need From The Agent To Do.🥅              ##
#############################################################
## BACKSTORY: Some Context For The Work. 📝                ##
#############################################################
## DESCRIPTION: The Details Of The Task.📚                 ##
#############################################################
## EXPECTED_OUTPUT: The Desired Output Of Task.📜          ##
#############################################################

class TaskSpecification(BaseModel):
    role:str
    goal:str
    backstory:str
    description:str
    expected_output:str
