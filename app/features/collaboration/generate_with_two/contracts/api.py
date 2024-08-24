from pydantic import BaseModel

class Response(BaseModel):
    report  : object
    history : object
    nodes   : object
    edges   : object


class Request(BaseModel):
    process_description: str
    addtional_user_ifo:str
    number_of_iterations : int