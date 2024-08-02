from ..models.types import ProcessReport,Diagram
from ..contracts.api import Request, Response

class Mapper:
    # constructor
    def __init__(self):
        pass

    # map the request to the input type of the service
    def map_to_service(self,request : Request) -> ProcessReport:
        return ProcessReport(content=request.process_description,
                             report=request.report)

    # map the output of the service to the type of the API response
    def map_from_service(self,output : Diagram) -> Response:
        return Response(connections=output.connections,annotations=output.annotations)