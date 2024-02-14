from __future__ import annotations

from typing import Any

from pydantic import BaseModel, model_validator

from models.answer import Answer

ANSWER_MAX = 75


class Question(BaseModel):
    statement: str
    answers: list[Answer] = []

    @model_validator(mode='before')
    @classmethod
    def validate(cls, data: Any) -> dict:
        if not isinstance(data, dict):
            raise ValueError('data must be dict')

        if set(data) != set(cls.model_fields):
            raise ValueError('wrong question format')

        data['statement'] = data['statement'].strip()

        if not data['statement']:
            raise ValueError('no statement')

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
