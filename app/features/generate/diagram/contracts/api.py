from pydantic import BaseModel
from ..models.types import Report

# the response that will be return via API
class Response(BaseModel):
    connections:object



class Request(BaseModel):
    process_description: str
    report:Report
    