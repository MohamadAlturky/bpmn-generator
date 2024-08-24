from pydantic import BaseModel

########################################
## the input type of the service       #
########################################

class ProcessDescription(BaseModel):
    content: str

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

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


#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


########################################
## the output type of the service      #
########################################

class Report(BaseModel):
    gateways_report:GatewaysReport
    tasks_report:TasksReport
    poolsLanes_report:PoolsLanesReport
    events_report:EventsReport


class ProcessReport(BaseModel):
    content: str
    report : Report


class Connections(BaseModel):
    connections:object
    
class Annotations(BaseModel):
    annotations:object
    
class Diagram(BaseModel):
    connections:object
    annotations:object
    report: Report
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#