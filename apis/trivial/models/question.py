from __future__ import annotations

from pydantic import BaseModel, model_validator

from models.answer import Answer


class Question(BaseModel):
    statement: str
    answers: list[Answer] = []

    @model_validator(mode='after')
    def check_passwords_match(self) -> Question:
        if not any(answer for answer in self.answers if answer.is_correct):
            raise ValueError('there must be at least one correct answer')
        return self
