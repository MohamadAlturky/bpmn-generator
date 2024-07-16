from ..models.types import  PoolsAndSwimlanes, ProcessDescription
from ..contracts.api import Request, Response

class Mapper:
    # constructor
    def __init__(self):
        pass

    # map the request to the input type of the service
    def map_to_service(self,request : Request) -> ProcessDescription:
        return ProcessDescription(content=request.process_description)

    # map the output of the service to the type of the API response
    def map_from_service(self,output) -> Response:
        return Response(nodes=output)