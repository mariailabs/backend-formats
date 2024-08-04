from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    id : int
    username : str

class TaxiBase(BaseModel):
    id: int
    town : str
    km : str
    time : str
    price : str
