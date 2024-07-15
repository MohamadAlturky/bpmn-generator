from core.res.result import Result
from ..models.types import LLMModelIn, LLMModelOut


# the service class for this slice
class Service:
    def __init__(self):
        pass

    def serve(self, request : LLMModelIn):
        return Result.success(LLMModelOut(nameLLMModelOut=request.nameLLMModelIn))