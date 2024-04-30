from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException

from modules.user.schemas.user import User as user_model
from modules.user.schemas.login import Login as login_model
from modules.user.controller.user_controller import UserController

from commons.http_status import http_status_code

user_route = APIRouter(prefix="/users")

user_controller = UserController()

@user_route.get("/", tags=["users"], status_code=200)
def get_users():
    users = user_controller.get_users()
    return JSONResponse(content=jsonable_encoder(obj=users), status_code=http_status_code['SUCCESS'])


@user_route.post("/", tags=["users"], status_code=201, response_model=dict)
def create_user(user: user_model):
    response = user_controller.create_user(user)
    print(response)
    return JSONResponse(content={"data": response["data"]}, status_code=response["code"])

@user_route.post("/login", tags=["auth"], status_code=200, response_model=dict)
def login(user: login_model):
    response = user_controller.login(user)
    return JSONResponse(content={"data": response["data"]}, status_code=response["code"])