from core.res.result import Result
from ..contracts.api import Request


def validate(request : Request) ->Result:
    if request.process_description == "":
        return Result.failure("the process description should not be empty.")
    if request.number_of_iterations <= 0:
        return Result.failure("the iteration should not be empty.")
    return Result.success()