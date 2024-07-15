from core.res.result import Result
from ..contracts.api import Request


def validate(request : Request) ->Result:
    if request.nameRequest == "":
        return Result.failure("the name should not be empty.")
    
    return Result.success()