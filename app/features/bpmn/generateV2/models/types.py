from pydantic import BaseModel

########################################
## the input type of the service       #
########################################

class QuestionDetails(BaseModel):
    process_description: str
    report: str
    notes: str

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

########################################
## some inner type used by the service #
########################################

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


########################################
## the output type of the service      #
########################################

class GeneratedResult(BaseModel):
    nodes  : object
    edges : object


#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#