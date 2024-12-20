from fastapi import FastAPI, HTTPException, Response
from starlette import status

import models
from models.question import Question, find_question_by_id, find_questions, insert_question

app = FastAPI()


@app.post('/question')
async def create_question(question: Question) -> Question:
    return await insert_question(question)


@app.get('/question/{id}')
async def read_question_by_id(id: str) -> Question:
    if not (question := await find_question_by_id(id)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question not found')

    return question


@app.get('/questions')
async def read_questions(author: str | None = None, limit: int | None = None) -> list[Question]:
    return await find_questions(author, limit)


@app.put('/question/{id}')
async def update_question(id: str, question: Question) -> Question:
    question.id = id
    if not (question := await models.question.update_question(question)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question not found')

    return question


@app.delete('/question/{id}')
async def delete_question(id: str) -> Response:
    await models.question.delete_question(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
