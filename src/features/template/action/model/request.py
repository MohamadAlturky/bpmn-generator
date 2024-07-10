from pydantic import BaseModel


class Request(BaseModel):
    name: str