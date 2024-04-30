from pydantic import BaseModel, Field

class Login(BaseModel):
    email: str = Field(min_length=10, max_length=30, pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    password: str = Field()

    class Config:
        json_schema_extra = {
            "example": {
                "email": "jane@doe.com",
                "password": "123123123",
            }
        }