from core.res.result import Result
from ..models.types import ProcessDescription,Report
from .tasks import generate_tasks_report
from .pools import generate_pools_lanes_report
from .events import generate_events_report
from .gateways import generate_gateways_report

# the service class for this slice
class Service:
    def __init__(self):
        pass

    def serve(self, request : ProcessDescription):
        tasks_result = generate_tasks_report(request)
        pools_result = generate_pools_lanes_report(request)
        events_result = generate_events_report(request)
        gateways_result = generate_gateways_report(request)

        if tasks_result.is_failure():
            return tasks_result
        if pools_result.is_failure():
            return pools_result
        if gateways_result.is_failure():
            return gateways_result
        if events_result.is_failure():
            return events_result
        
        
        
        return Result.success(Report(
            events_report=events_result.value,
            gateways_report=gateways_result.value,
            poolsLanes_report=pools_result.value,
            tasks_report=tasks_result.value
        ))