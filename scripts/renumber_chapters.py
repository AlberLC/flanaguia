import re
import zipfile
from pathlib import Path

CHAPTER_PATTERN = re.compile(r'##\s*\d*\.?\s*(.*)')
EXERCISE_DIRECTORY_PATTERN = re.compile(r'_\d+$')
EXERCISE_NUMBER_PATTERN = re.compile(r'^\d+')
EXERCISES_PATH = Path('../exercises')
MARKDOWN_PATH = EXERCISES_PATH / 'README.md'


def main() -> None:
    lines = []
    current_chapter = ''
    previous_exercise_number = 0
    exercise_number = 0
    new_zip_paths = []

    with open(MARKDOWN_PATH, encoding='utf-8') as file:
        for line in file:
            if match := CHAPTER_PATTERN.match(line):
                current_chapter = match.group(1).strip()
                exercise_number = 0

            if match := EXERCISE_NUMBER_PATTERN.match(line):
                previous_exercise_number = int(match.group())
                exercise_number += 1
                line = EXERCISE_NUMBER_PATTERN.sub(str(exercise_number), line)

            if exercise_number != previous_exercise_number and '[zip]' in line:
                if new_zip_path := rename_zip(
                    f'{current_chapter.lower().replace(' ', '_')}_{previous_exercise_number}',
                    exercise_number
                ):
                    new_zip_paths.append(new_zip_path)

            lines.append(line)

    for new_zip_path in new_zip_paths:
        new_zip_path.rename(new_zip_path.with_stem(new_zip_path.stem.removesuffix('_')))

    MARKDOWN_PATH.write_text(''.join(lines), encoding='utf-8', newline='\n')


def rename_zip(previous_exercise_directory_name: str, new_exercise_number: int) -> Path | None:
    previous_zip_path = (EXERCISES_PATH / previous_exercise_directory_name).with_suffix('.zip')

    if not previous_zip_path.is_file():
        return

    new_exercise_directory_name = EXERCISE_DIRECTORY_PATTERN.sub(
        f'_{new_exercise_number}',
        previous_exercise_directory_name
    )
    new_zip_path = EXERCISES_PATH / f'{new_exercise_directory_name}_.zip'

    with zipfile.ZipFile(previous_zip_path) as previous_zip_file, zipfile.ZipFile(new_zip_path, 'w') as new_zip_file:
        for zip_info in previous_zip_file.infolist():
            data = previous_zip_file.read(zip_info.filename)
            zip_info.filename = zip_info.filename.replace(
                previous_exercise_directory_name,
                new_exercise_directory_name,
                count=1
            )
            new_zip_file.writestr(zip_info, data)

    previous_zip_path.unlink()

    return new_zip_path


main()
