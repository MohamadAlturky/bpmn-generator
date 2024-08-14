#########################################
## import libraries 📕📗📘📙📔📗📘📒📚##
#########################################

##🔗 from python
from http import HTTPStatus
import os
from fastapi import APIRouter
from fastapi import HTTPException

##🔗 from application core
from core.paths.get_parent import get_parent_folders
from core.res.result import Result

##🔗 from the same slice
from ..service.logic import Service
from ..contracts.api import Request
from ..validator.applier import validate
from ..mapping.mapper import Mapper
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

#########################################
## responsibility : build the route    ##
#########################################
current_file_path = os.path.abspath(__file__)
# print(current_file_path)
parent_folders = get_parent_folders(current_file_path)

print("Parent folders:", parent_folders)

#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#



#########################################
## this will be changed for each slice ##
#########################################
## responsibility : create the router  ##
#########################################

router = APIRouter(
    prefix=f"/{parent_folders[2]}"
)
#☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#

#########################################
## this will be changed for each slice ##
#########################################
## responsibility: define the endpoint ##
#########################################

@router.post(f"/{parent_folders[1]}")
def report(request:Request):
    
    #########################################
    ## First Step    🔍🔍🔍🔍            ##
    #########################################
    ## responsibility : request validation ##
    #########################################
    validation_result : Result = validate(request)
    
    if validation_result.is_failure():
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail=validation_result.error)
    #☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#
    
    
    #########################################
    ## Second Step    🔖🔖🔖🧷🧷🧷      ##
    #########################################
    ## responsibility : request mapping    ##
    #########################################
    
    mapper = Mapper()
    inputs = mapper.map_to_service(request)
    #☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#
    
    
    #########################################
    ## Third Step    🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻    ##
    #########################################
    ## responsibility : run the service    ##
    #########################################

    service = Service()
    result = service.serve(inputs)
    
    # try:
    #     result = service.serve(inputs)
    # except Exception:
    #     raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,detail="error happend sorry")
    #☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#
    
    #########################################
    ## Fourth Step       ✅|❌            ##
    #########################################
    ## responsibility: respond to client   ##
    #########################################
    
    if result.is_failure():
            raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,detail=result.error)

    # return the mapped response
    return mapper.map_from_service(result.value)
    #☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️#
    

## NOTE 📋:
###🔗 The Advantages🥳 of This design:
    ##-💪🏻 respects single responsibility princible
    ##-💪🏻 respects fail early pattern 
    ##-💪🏻 considered open for extension close for modification 
    ##-💪🏻 respects the High Cohesion princible between the components of the same module   
    
###🔗 The Disadvantages😓 of this design:
    ##-👎🏽 considered High Coupled Module, so there is coupling between the components of the same module
    ##-👎🏽 considered Less Reusable than clean architecture