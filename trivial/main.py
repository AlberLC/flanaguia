import pathlib

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse


def find_environment_variables(path: str | pathlib.Path) -> dict:
    return dict(
        line.split('=', maxsplit=1) for original_line in pathlib.Path(path).read_text().splitlines()
        if '=' in (line := original_line.strip()) and not line.startswith('#')
    )


sub_app = FastAPI()

app = FastAPI()
app.mount('/flanatrigo', sub_app)


@sub_app.get('/download', response_class=FileResponse)
async def root():
    return FileResponse('FlanaTrigo.zip', filename='FlanaTrigo.zip')


@sub_app.get('/version')
async def root():
    return pathlib.Path('version').read_text()


if __name__ == '__main__':
    uvicorn.run('main:app')
