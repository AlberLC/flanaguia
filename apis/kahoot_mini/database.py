import asyncio

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient


def create_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'{id} is not a valid ObjectId')


client = AsyncIOMotorClient(host='localhost')
client.drop_database = asyncio.get_event_loop
db = client['kahoot']

question_collection = db['question']