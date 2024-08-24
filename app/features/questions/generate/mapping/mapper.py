from ..models.types import GeneratedResult, QuestionDetails
from ..contracts.api import Request, Response

class Mapper:
    # constructor
    def __init__(self):
        pass

    # map the request to the input type of the service
    def map_to_service(self, request : Request) -> QuestionDetails:
        return QuestionDetails(process_description=request.process_description)

    # map the output of the service to the type of the API response
    def map_from_service(self, output : GeneratedResult) -> Response:
        return Response(questions=output.questions)