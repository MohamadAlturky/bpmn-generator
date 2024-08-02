from pydantic import BaseModel


########################################
## some inner type used by the service #
########################################

class EventsReport(BaseModel):
    content: object

class PoolsLanesReport(BaseModel):
    content: object

class TasksReport(BaseModel):
    content: object

class GatewaysReport(BaseModel):
    content: object

class Report(BaseModel):
    gateways_report:GatewaysReport
    tasks_report:TasksReport
    poolsLanes_report:PoolsLanesReport
    events_report:EventsReport
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


########################################
## the output type of the service      #
########################################

class Connections(BaseModel):
    connections:object
    
class Annotations(BaseModel):
    annotations:object
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#



########################################
## the input type of the service       #
########################################

class ProcessReport(BaseModel):
    content: str
    report : Report

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#