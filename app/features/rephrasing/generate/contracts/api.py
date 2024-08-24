from pydantic import BaseModel

class Response(BaseModel):
    notes  : object
    process_description : object


class Request(BaseModel):
    process_description: str