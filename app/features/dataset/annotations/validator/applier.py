from core.res.result import Result
from ..contracts.api import Request


def validate(request : Request) ->Result:
    return Result.success()