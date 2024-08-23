from core.res.result import Result
from ..contracts.api import Request


def validate(request : Request) ->Result:
    if request.process_description == "":
        return Result.failure("the process description should not be empty.")
    
    if request.report == None:
        return Result.failure("the events, gateways, pools and tasks should not be empty.")
    
    return Result.success()