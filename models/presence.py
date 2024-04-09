from pydantic import BaseModel
from enum import Enum

class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    role: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    role: str
    hashed_password: str

class PresenceEnum(str, Enum):
    presente = "presente"
    falta = "falta"

class Presence(BaseModel):
    prof: str
    student: str
    presence: PresenceEnum
