from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from models.question import Question
from models.user import User, find_user_by_name, get_current_user, get_users, update_user

STATEMENT_MAX = 120
TEMPLATE_LENGTH = 11

router = APIRouter()


@router.post('/question')
async def create_question(
    question: Question,
    current_user: Annotated[User, Depends(get_current_user)]
) -> User:
    if len(current_user.name) + TEMPLATE_LENGTH + len(question.statement) > STATEMENT_MAX:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='author and/or statement too long')

    current_user.questions.append(question)
    return await update_user(current_user)


@router.get('/questions')
@router.get('/questions/{name}')
async def read_questions(name: str | None = None) -> list[Question]:
    if name:
        if user := await find_user_by_name(name):
            return user.questions
        else:
            return []
    else:
        return [question for user in await get_users() for question in user.questions]
