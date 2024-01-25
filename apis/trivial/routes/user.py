import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status

import models
from models.login_data import LoginData
from models.user import User, find_user_by_id, find_user_by_name, get_users, insert_user, validate_user_permission
from security import compare_digest, create_key, encode_jwt_token, hash_password

router = APIRouter()


@router.post('/sign_in')
async def sign_in(login_data: LoginData) -> dict:
    if await find_user_by_name(login_data.username):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User already exists')

    salt = create_key()
    hashed_password = hash_password(login_data.password, salt)
    await insert_user(User(name=login_data.username, hashed_password=hashed_password, salt=salt))

    return await log_in(login_data)


@router.get('/log_in')
async def log_in(login_data: LoginData) -> dict:
    user = await read_user_by_name(name=login_data.username)
    hashed_password = hash_password(login_data.password, user.salt)
    if not compare_digest(hashed_password.encode(), user.hashed_password.encode()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    payload = {
        'sub': login_data.username,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(weeks=1)
    }

    return {'access_token': encode_jwt_token(payload), 'token_type': 'bearer'}


@router.get('/user/{id}')
async def read_user_by_id(id: str) -> User:
    if not (user := await find_user_by_id(id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return user


@router.get('/user')
async def read_user_by_name(name: str) -> User:
    if not (user := await find_user_by_name(name)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return user


@router.get('/users')
async def read_users(limit: int | None = None) -> list[User]:
    return await get_users(limit)


@router.put('/user/{id}')
async def update_user(user: User, current_user: Annotated[User, Depends(validate_user_permission)]) -> User:
    user.id = current_user.id
    return await models.user.update_user(user)


@router.delete('/user/{id}')
async def delete_user(current_user: Annotated[User, Depends(validate_user_permission)]) -> Response:
    await models.user.delete_user(current_user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
