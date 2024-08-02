from core.res.result import Result
from ..models.types import Connections,ProcessReport
from .diagrams import generate_connections_report

# the service class for this slice
class Service:
    def __init__(self):
        pass

    def serve(self, request : ProcessReport):
        connections_result = generate_connections_report(request)

        if connections_result.is_failure():
            return connections_result
        
        
        return Result.success(Connections(connections=connections_result.value))