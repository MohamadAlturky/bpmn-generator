from pydantic import BaseModel
########################################
## the input type of the service       #
########################################

class ProcessDescription(BaseModel):
    content: str

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

########################################
## some inner type used by the service #
########################################

class Swimlane(BaseModel):
    name : str

class Pool(BaseModel):
    name: str
    swimlanes: list[Swimlane]

class PoolsAndSwimlanes(BaseModel):
    pools: list[Pool]

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#