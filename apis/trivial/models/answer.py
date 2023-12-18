from pydantic import BaseModel


class Answer(BaseModel):
    text: str
    is_correct: bool = False
