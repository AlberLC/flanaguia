from typing import Annotated, Any

from pydantic import BaseModel, BeforeValidator, Field, model_validator
from pymongo import ReturnDocument

from database import create_object_id, question_collection
from models.answer import Answer

ANSWER_MAX = 75
STATEMENT_MAX = 120
TEMPLATE_LENGTH = 11


class Question(BaseModel):
    id: Annotated[str, BeforeValidator(str)] | None = Field(alias='_id', default=None)
    author: str
    statement: str
    answers: list[Answer] = []

    @model_validator(mode='before')
    @classmethod
    def validate(cls, data: Any) -> dict:
        if not isinstance(data, dict):
            raise ValueError('data must be dict')

        if {*data, 'id', '_id'} != {*cls.model_fields, '_id'}:
            raise ValueError('wrong question format')

        data['author'] = data['author'].strip()
        data['statement'] = data['statement'].strip()

        if not data['author']:
            raise ValueError('no author')

        if not data['statement']:
            raise ValueError('no statement')

        if len(data['author']) + TEMPLATE_LENGTH + len(data['statement']) > STATEMENT_MAX:
            raise ValueError('author and/or statement too long')

        if not 2 <= len(data['answers']) <= 4:
            raise ValueError('wrong number of answers')

        correct_answers = 0
        for answer_data in data['answers']:
            if {*answer_data, 'is_correct'} != set(Answer.model_fields):
                raise ValueError('wrong answer format')

            answer_data['text'] = answer_data['text'].strip()
            if not 0 < len(answer_data['text']) <= ANSWER_MAX:
                raise ValueError('wrong answer length')

            if answer_data.get('is_correct', False):
                correct_answers += 1

        if not correct_answers:
            raise ValueError('no correct answers')

        return data


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
