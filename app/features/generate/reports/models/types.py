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
    json: object


class PoolsLanesReport(BaseModel):
    json: object


class TasksReport(BaseModel):
    json: object


class GatewaysReport(BaseModel):
    json: object

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#


########################################
## the output type of the service      #
########################################

class Report(BaseModel):
    gateways_report:GatewaysReport
    tasks_report:TasksReport
    poolsLanes_report:PoolsLanesReport
    events_report:EventsReport
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#