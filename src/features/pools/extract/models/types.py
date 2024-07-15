from pydantic import BaseModel

# the input type of the service
class LLMModelIn(BaseModel):
    nameLLMModelIn: str
    

# the output type of the service
class LLMModelOut(BaseModel):
    nameLLMModelOut: str


# some inner type used by the service
class LLMModelInner(BaseModel):
    nameLLMModelInner: str
