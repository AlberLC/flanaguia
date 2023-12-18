from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import JWTError
from pydantic import BaseModel, BeforeValidator, Field
from pymongo import ReturnDocument

from database import create_object_id, user_collection
from models.question import Question
from security import decode_jwt_token, get_bearer_token


class User(BaseModel):
    id: Annotated[str, BeforeValidator(str)] | None = Field(alias='_id', default=None)
    name: str
    hashed_password: str
    salt: str
    questions: list[Question] = []

    def __eq__(self, other) -> bool:
        return isinstance(other, User) and self.id == other.id


async def delete_user(id: str) -> None:
    await user_collection.delete_one({'_id': create_object_id(id)})


async def find_user_by_id(id: str) -> User | None:
    if user_document := await user_collection.find_one({'_id': create_object_id(id)}):
        return User(**user_document)


async def find_user_by_name(name: str) -> User | None:
    if user_document := await user_collection.find_one({'name': name}):
        return User(**user_document)


async def get_current_user(token: Annotated[str, Depends(get_bearer_token)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = decode_jwt_token(token)
    except JWTError:
        raise credentials_exception

    if not (username := payload.get('sub')) or not (user := await find_user_by_name(username)):
        raise credentials_exception

    return user


async def get_users(limit: int | None = None) -> list[User]:
    cursor = user_collection.find()
    if limit is not None:
        cursor.limit(limit)

    return [User(**user_document) async for user_document in cursor]


async def insert_user(user: User) -> User:
    insertion_result = await user_collection.insert_one(user.model_dump(exclude_none=True))
    return await find_user_by_id(insertion_result.inserted_id)


async def update_user(user: User) -> User:
    user_document = await user_collection.find_one_and_update(
        {'_id': create_object_id(user.id)},
        {'$set': user.model_dump(exclude={'id'})},
        return_document=ReturnDocument.AFTER
    )
    return User(**user_document)


async def validate_user_permission(id: str, current_user: Annotated[User, Depends(get_current_user)]) -> User:
    if not (target_user := await find_user_by_id(id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    elif target_user != current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return current_user
