## imports from lib
from http import HTTPStatus
from fastapi import APIRouter
from fastapi import HTTPException

## imports from application core
from core.res.result import Result

## imports from the same slice
from ..service.logic import Service
from ..model.request import Request
from ..validator.applier import validate

## create the router
router = APIRouter(
    prefix="/template"
)

## define the endpoint
@router.post("/action")
def extract_pools(request:Request):
    
    # step 1 : request validation
    validation_result : Result = validate(request)
    
    if validation_result.is_failure():
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail=validation_result.error)
    
    # step 2 : get the response from the service
    service = Service()
    try:
        result : Result = service.run(request)
    except Exception:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail="error happend sorry")
    
    # step 3 : return the appropriate response
    if result.is_failure():
            raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,detail=result.error)
    
    return result.value
