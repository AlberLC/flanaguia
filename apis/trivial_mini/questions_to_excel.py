import asyncio

import openpyxl

from models.question import find_questions

FILE_PATH = 'KahootQuizTemplate.xlsx'
AUTHORS = ['juan']
SECONDS_LIMIT = 60

STATEMENT_COLUMN = 'B'
ANSWER_COLUMNS = ('C', 'D', 'E', 'F')
TIME_COLUMN = 'G'
CORRECT_COLUMN = 'H'

INITIAL_ROW = 9


async def main():
    workbook = openpyxl.load_workbook(FILE_PATH)
    worksheet = workbook.active

    current_row = INITIAL_ROW
    for question in await find_questions():
        correct_answers = [str(i) for i, answer in enumerate(question.answers, start=1) if answer.is_correct]
        if question.author not in AUTHORS or len(question.answers) < 2 or not correct_answers:
            continue

        worksheet[f'{STATEMENT_COLUMN}{current_row}'] = f'{question.author} pregunta: {question.statement}'
        for column, answer in zip(ANSWER_COLUMNS, question.answers):
            worksheet[f'{column}{current_row}'] = answer.text
        worksheet[f'{TIME_COLUMN}{current_row}'] = SECONDS_LIMIT
        worksheet[f'{CORRECT_COLUMN}{current_row}'] = ','.join(correct_answers)

        current_row += 1

    workbook.save(FILE_PATH)


asyncio.run(main())
