from core.res.result import Result
from ..models.types import Connections,ProcessReport,Diagram
from .diagrams import generate_connections_report
from .pools import generate_annotations_report

# the service class for this slice
class Service:
    def __init__(self):
        pass

    def serve(self, request : ProcessReport):
        connections_result = generate_connections_report(request)

        if connections_result.is_failure():
            return connections_result
        
        annotations_results = generate_annotations_report(process_report=request,connections=connections_result.value)

        if annotations_results.is_failure():
            return annotations_results
        
        
        # return Result.success(Connections(connections=connections_result.value))
        return Result.success(Diagram(connections=connections_result.value,
                                      annotations=annotations_results.value))