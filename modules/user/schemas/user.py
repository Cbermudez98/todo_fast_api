from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=3, max_length=10)
    last_name: str = Field(min_length=3, max_length=20)
    email: str = Field(min_length=10, max_length=30, pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    password: str = Field(min_length=6, max_length=30)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Jane",
                "last_name": "Doe",
                "email": "jane@doe.com",
                "password": "123123123",
            }
        }