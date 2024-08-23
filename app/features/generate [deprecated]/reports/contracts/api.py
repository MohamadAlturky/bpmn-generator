from pydantic import BaseModel


# the response that will be return via API
class Response(BaseModel):
    report:object



class Request(BaseModel):
    process_description: str