from pydantic import BaseModel


class User_dto(BaseModel):
    email: str
    login: str
    passwword: str
