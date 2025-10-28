import re
import shutil
import zipfile
from pathlib import Path

EXERCISES_PATH = Path('../exercises')
MARKDOWN_PATH = EXERCISES_PATH / 'README.md'


def rename_zip(exercise_directory_name: str, new_exercise_number: int) -> None:
    previous_exercise_directory = EXERCISES_PATH / exercise_directory_name
    previous_zip_path = previous_exercise_directory.with_suffix('.zip')

    if not previous_zip_path.is_file():
        return

    with zipfile.ZipFile(previous_zip_path) as zip_file:
        zip_file.extractall(EXERCISES_PATH)

    new_exercise_directory = Path(re.sub(r'_\d+$', f'_{new_exercise_number}', str(previous_exercise_directory)))
    new_zip_path = new_exercise_directory.with_suffix('.zip')

    with zipfile.ZipFile(new_zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for path in previous_exercise_directory.rglob('*'):
            if path.is_file():
                zip_file.write(path, new_exercise_directory.name / path.relative_to(previous_exercise_directory))

    shutil.rmtree(previous_exercise_directory)
    previous_zip_path.unlink()


lines = []
current_chapter: str | None = None
previous_exercise_number: int | None = None
exercise_number = 0

with open(MARKDOWN_PATH, encoding='utf-8') as file:
    for line in file:
        if line.lstrip().startswith('##'):
            current_chapter = line.split('##')[1].strip()
            exercise_number = 0

        if match := re.match(r'\d+', line):
            previous_exercise_number = int(match.group())
            exercise_number += 1
            line = re.sub(r'^\d+', str(exercise_number), line)

        if exercise_number != previous_exercise_number and '[zip]' in line:
            rename_zip(f'{current_chapter.lower().replace(' ', '_')}_{previous_exercise_number}', exercise_number)

        lines.append(line)

MARKDOWN_PATH.write_text(''.join(lines), encoding='utf-8', newline='\n')
