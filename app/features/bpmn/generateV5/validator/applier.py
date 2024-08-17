from core.res.result import Result
from ..contracts.api import Request


def validate(request : Request) ->Result:
    if request.process_description == "":
        if request.report == "":
            return Result.failure("the process description and the report should not be empty.")
    return Result.success()