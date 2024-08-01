from pydantic import BaseModel


# the response that will be return via API
class Response(BaseModel):
    resultResponse:str



# the request that will be bound from the request body
class Request(BaseModel):
    nameRequest: str