from pydantic import BaseModel

class Swimlane(BaseModel):
    name:str

class Pool(BaseModel):
    name:str
    swimlanes:list[Swimlane]

class Pools(BaseModel):
    pools: list[Pool]
