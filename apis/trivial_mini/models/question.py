from typing import Annotated

from pydantic import BaseModel, BeforeValidator, Field
from pymongo import ReturnDocument

from database import create_object_id, question_collection
from models.answer import Answer


class Question(BaseModel):
    id: Annotated[str, BeforeValidator(str)] | None = Field(alias='_id', default=None)
    author: str
    statement: str
    answers: list[Answer] = []


async def delete_question(id: str) -> None:
    await question_collection.delete_one({'_id': create_object_id(id)})


async def find_question_by_id(id: str) -> Question | None:
    if question_document := await question_collection.find_one({'_id': create_object_id(id)}):
        return Question(**question_document)


async def find_questions(author: str | None = None, limit: int | None = None) -> list[Question]:
    kwargs = {}

    if author:
        kwargs['filter'] = {'author': author}

    if limit:
        kwargs['limit'] = limit

    cursor = question_collection.find(**kwargs)
    return [Question(**question_document) async for question_document in cursor]


async def insert_question(question: Question) -> Question:
    insertion_result = await question_collection.insert_one(question.model_dump(exclude={'id'}))
    return await find_question_by_id(insertion_result.inserted_id)


async def update_question(question: Question) -> Question | None:
    if question_document := await question_collection.find_one_and_update(
        {'_id': create_object_id(question.id)},
        {'$set': question.model_dump(exclude={'id'})},
        return_document=ReturnDocument.AFTER
    ):
        return Question(**question_document)
