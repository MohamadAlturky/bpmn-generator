from core.res.result import Result
from ..res.response import Response
from ..model.request import Request


class Service:
    def __init__(self):
        pass
    
    def run(self, request : Request) -> Result:
        return Result.success(Response(result=request.name))