from pydantic import BaseModel

class Response(BaseModel):
    nodes  : object
    edges : object
    

class Request(BaseModel):
    process_description: str
    report: str
    notes: str