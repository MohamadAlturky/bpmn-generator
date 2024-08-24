from pydantic import BaseModel


class Response(BaseModel):
    nodes  : object
    edges : object

class Request(BaseModel):
    row_num: int