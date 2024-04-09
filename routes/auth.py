from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from models.presence import User, CreateUserRequest
from config.database import collection_user
from schema.schemas import userlist_serial, users_serial
from passlib.context import CryptContext
from pymongo.collection import Collection
from jose import jwt, JWTError
from starlette import status
from bson import ObjectId


auth = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = 'bfddc6059c94aa78f1f3d8be33cbdcf0894e5d8bb8960f6d3d8d3d60eecd43c9'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


def authenticate_user(username: str, password: str, collection_user: Collection):
    user = collection_user.find_one({"username": username})
    if not user:
        return False
    if not bcrypt_context.verify(password, user['hashed_password']):
        return False
    return user
    

def create_access_token(username: str, expires_delta: timedelta):
    encode = {'sub': username}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
        return {'username': username}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')


# GET Request Method
@auth.get("/users")
async def get_user():
    users = userlist_serial(collection_user.find())
    return users


# POST Request Method
@auth.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest):
    create_user_model = User (
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
    )

    collection_user.insert_one(dict(create_user_model))

    return create_user_model


@auth.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password, collection_user)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    token = create_access_token(user['username'], timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}


# PUT Request Method
    

# DELETE Request Method
    