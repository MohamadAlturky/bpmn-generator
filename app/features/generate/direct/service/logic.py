import concurrent.futures
from core.res.result import Result
from ..models.types import ProcessDescription,Report,GatewaysReport,EventsReport,PoolsLanesReport,TasksReport
from .tasks import generate_tasks_report
from .pools import generate_pools_lanes_report
from .events import generate_events_report
from .gateways import generate_gateways_report
from .diagrams import generate_connections_report
from .components import generate_annotations_report
from  ..models.types import ProcessReport, Diagram

# the service class for this slice
class Service:
    def __init__(self):
        pass

    def serve(self, request : ProcessDescription):
        # tasks_result = generate_tasks_report(request)
        # pools_result = generate_pools_lanes_report(request)
        # events_result = generate_events_report(request)
        # gateways_result = generate_gateways_report(request)
        
        pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)

        tasks_result_future = pool.submit(lambda : generate_tasks_report(request))
        pools_result_future = pool.submit(lambda : generate_pools_lanes_report(request))
        events_result_future = pool.submit(lambda : generate_events_report(request))
        gateways_result_future = pool.submit(lambda : generate_gateways_report(request))
        
        tasks_result = tasks_result_future.result()
        pools_result = pools_result_future.result()
        events_result = events_result_future.result()
        gateways_result = gateways_result_future.result()
        
        if tasks_result.is_failure():
            return tasks_result
        if pools_result.is_failure():
            return pools_result
        if gateways_result.is_failure():
            return gateways_result
        if events_result.is_failure():
            return events_result

        report = Report(
            gateways_report=GatewaysReport(content=gateways_result.value),
            tasks_report=TasksReport(content=tasks_result.value),
            poolsLanes_report=PoolsLanesReport(content=pools_result.value),
            events_report=EventsReport(content=events_result.value)
        )
        
        process_report = ProcessReport(content=request.content,report=report)      
          
        connections_result = generate_connections_report(process_report=process_report)

        if connections_result.is_failure():
            return connections_result
        
        annotations_results = generate_annotations_report(process_report=process_report,connections=connections_result.value)

        if annotations_results.is_failure():
            return annotations_results
        
        
        return Result.success(Diagram(connections=connections_result.value,
                                      annotations=annotations_results.value,
                                      report=report))