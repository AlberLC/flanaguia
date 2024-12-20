from pydantic import BaseModel


class LoginData(BaseModel):
    username: str
    password: str
