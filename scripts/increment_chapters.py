import re
from pathlib import Path

FIRST_LINE = 620
LAST_LINE = 2155
PATH = Path('../exercises/README.md')


def add_one(match: re.Match[str]) -> str:
    return f'{int(match.group()) + 1}'


text = PATH.read_text(encoding='utf-8')

lines = []

for i, line in enumerate(text.splitlines()):
    if FIRST_LINE <= i <= LAST_LINE:
        line = re.sub(r'^\d+', add_one, line)

    lines.append(line)

PATH.write_text(f'{'\n'.join(lines)}\n', encoding='utf-8', newline='\n')
