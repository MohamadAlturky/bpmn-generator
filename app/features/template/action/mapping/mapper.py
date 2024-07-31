from ..models.types import LLMModelIn, LLMModelOut
from ..contracts.api import Request, Response

class Mapper:
    # constructor
    def __init__(self):
        pass

    # map the request to the input type of the service
    def map_to_service(self,request : Request) -> LLMModelIn:
        return LLMModelIn(nameLLMModelIn=request.nameRequest)

    # map the output of the service to the type of the API response
    def map_from_service(self,output : LLMModelOut) -> Response:
        return Response(resultResponse=output.nameLLMModelOut)