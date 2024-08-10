from typing import List
from pydantic import BaseModel

from ..models.types import Question

    
class Response(BaseModel):
    questions:List[Question]


class Request(BaseModel):
    process_description: str