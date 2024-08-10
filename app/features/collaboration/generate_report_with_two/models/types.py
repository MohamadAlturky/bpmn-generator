from pydantic import BaseModel

########################################
## the input type of the service       #
########################################

class QuestionDetails(BaseModel):
    process_description: str
    addtional_user_info:str
    number_of_iterations : int

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

########################################
## some inner type used by the service #
########################################

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


########################################
## the output type of the service      #
########################################

class GeneratedResult(BaseModel):
    report  : object
    history : object
    nodes   : object
    edges   : object

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#