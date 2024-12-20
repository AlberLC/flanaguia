import asyncio
import itertools
import random

import openpyxl
import openpyxl.worksheet.worksheet

from models.user import get_users

FILE_PATH = 'KahootQuizTemplate.xlsx'
N_QUESTIONS: int | None = None
SECONDS_LIMIT = 60

STATEMENT_COLUMN = 'B'
ANSWER_COLUMNS = ('C', 'D', 'E', 'F')
TIME_COLUMN = 'G'
CORRECT_COLUMN = 'H'
MAX_ANSWERS = 4
CLEAN_ROWS = 100

INITIAL_ROW = 9


# noinspection PyTypeChecker
def clean_rest(
    worksheet: openpyxl.worksheet.worksheet.Worksheet,
    current_row: int,
    clean_rows: int = CLEAN_ROWS
) -> None:
    for _ in range(clean_rows):
        worksheet[f'{STATEMENT_COLUMN}{current_row}'] = None
        for column in ANSWER_COLUMNS:
            worksheet[f'{column}{current_row}'] = None
        worksheet[f'{TIME_COLUMN}{current_row}'] = None
        worksheet[f'{CORRECT_COLUMN}{current_row}'] = None
        current_row += 1


async def main() -> None:
    workbook = openpyxl.load_workbook(FILE_PATH)
    worksheet = workbook.active

    users = await get_users()
    questions_data = []
    for user in users:
        question_data = {'author': user.name}
        for question in user.questions:
            question_data |= dict(question)
            questions_data.append(question_data)

    if N_QUESTIONS is not None and len(questions_data) > N_QUESTIONS:
        questions_data = random.sample(questions_data, N_QUESTIONS)

    entered_questions = set()
    current_row = INITIAL_ROW
    for question_data in questions_data:
        correct_answers = [
            str(i) for i, answer in enumerate(question_data['answers'][:MAX_ANSWERS], start=1) if answer.is_correct
        ]
        question_mark = (
            question_data['author'],
            question_data['statement'],
            tuple(tuple(dict(answer).values()) for answer in question_data['answers'][:MAX_ANSWERS])
        )
        if len(question_data['answers']) < 2 or not correct_answers or question_mark in entered_questions:
            continue

        worksheet[f'{STATEMENT_COLUMN}{current_row}'] = f"{question_data['author']} pregunta: {question_data['statement']}"
        for column, answer in itertools.zip_longest(ANSWER_COLUMNS, question_data['answers'][:MAX_ANSWERS]):
            worksheet[f'{column}{current_row}'] = answer.text if answer else None
        worksheet[f'{TIME_COLUMN}{current_row}'] = SECONDS_LIMIT
        worksheet[f'{CORRECT_COLUMN}{current_row}'] = ','.join(correct_answers)

        entered_questions.add(question_mark)
        current_row += 1

    clean_rest(worksheet, current_row)

    workbook.save(FILE_PATH)


asyncio.run(main())
