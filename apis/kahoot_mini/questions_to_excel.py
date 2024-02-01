import asyncio
import itertools
import random

import openpyxl
import openpyxl.worksheet.worksheet

from models.question import find_questions

FILE_PATH = 'KahootQuizTemplate.xlsx'
AUTHORS = []
N_QUESTIONS = 30
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

    if len(questions := await find_questions()) > N_QUESTIONS:
        questions = random.sample(questions, N_QUESTIONS)

    current_row = INITIAL_ROW
    for question in questions:
        correct_answers = [str(i) for i, answer in enumerate(question.answers, start=1) if answer.is_correct]
        if question.author not in AUTHORS or len(question.answers) < 2 or not correct_answers:
            continue

        worksheet[f'{STATEMENT_COLUMN}{current_row}'] = f'{question.author} pregunta: {question.statement}'
        for column, answer in itertools.zip_longest(ANSWER_COLUMNS, question.answers[:MAX_ANSWERS]):
            worksheet[f'{column}{current_row}'] = answer.text if answer else None
        worksheet[f'{TIME_COLUMN}{current_row}'] = SECONDS_LIMIT
        worksheet[f'{CORRECT_COLUMN}{current_row}'] = ','.join(correct_answers)

        current_row += 1

    clean_rest(worksheet, current_row)

    workbook.save(FILE_PATH)


asyncio.run(main())
