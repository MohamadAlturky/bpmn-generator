from pydantic import BaseModel
from ..models.types import Pool

# the response that will be return via API
class Response(BaseModel):
    # pools: list[Pool]
    nodes: object



# the request that will be bound from the request body
class Request(BaseModel):
    process_description: str