from typing import List
from sqlalchemy.exc import IntegrityError 

from modules.user.schemas.user import User as user_schema
from modules.user.schemas.login import Login as login_schema
from config.database import Session
from modules.user.models.user_model import User as user_model
from commons.http_status import http_status_code
from utils.bcrypt import Bcrypt
from utils.jwt import Jwt

class UserController():
    def __init__(self) -> None:
        self.session = Session()
        self.bcrypt = Bcrypt()
        self.jwt = Jwt()
        # self.__private_users: List[UserModel] = []

    def create_user(self, user: user_schema) -> dict:
        try:
            new_pwd = self.bcrypt.encrypt(user.password)
            user.password = new_pwd
            new_user = user_model(**user.model_dump())
            self.session.add(new_user)
            self.session.commit()
            user_dict = {
                "id": new_user.id,
                "name": new_user.name,
                "last_name": new_user.last_name,
                "email": new_user.email
            }
            return { "code": http_status_code["CREATED"], "data": user_dict }
        except IntegrityError as error:
            self.session.rollback()
            return { "code": http_status_code["DUPLICATE_RECORD"], "data": "email already exists" }
        except Exception as error:
            print(error)
            return { "code": http_status_code["INTERNAL_SERVER_ERROR"], "data": "internal server error" }

    def get_users(self) -> List[user_schema]:
        users = self.session.query(user_model).all()
        self.session.close()
        return users
    
    def login(self, user: login_schema) -> str:
        try:
            user_found = self.session.query(user_model).filter(user_model.email == user.email).first()
            if user_found is None:
                return { "code": http_status_code["NOT_FOUND"], "data": "user not found" }
            
            is_valid_pwd = self.bcrypt.compare(encrypted=user_found.password, password=user.password)
            if is_valid_pwd != True:
                return { "code": http_status_code["FORBIDDEN"], "data": "password not matching" }
            token = self.jwt.encode({ "id": user_found.id })
            print(token)
            return { "code": http_status_code["SUCCESS"], "data": token }
        except Exception as error:
            print(error)
            return {}