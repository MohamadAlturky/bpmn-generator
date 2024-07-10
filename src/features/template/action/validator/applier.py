from core.res.result import Result
from ..model.request import Request


def validate(request : Request) ->Result:
    if request.name == "":
        return Result.failure("the name should not be empty.")
    
    return Result.success()