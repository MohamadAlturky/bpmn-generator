from typing import List
from pydantic import BaseModel

########################################
## the input type of the service       #
########################################

class QuestionDetails(BaseModel):
    process_description: str

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

########################################
## some inner type used by the service #
########################################

class Question(BaseModel):
    question:str
    
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


########################################
## the output type of the service      #
########################################

class GeneratedResult(BaseModel):
    questions:List[Question]
    

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#