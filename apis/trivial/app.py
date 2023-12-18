from fastapi import FastAPI

import routes.question
import routes.user

app = FastAPI()

app.include_router(routes.question.router)
app.include_router(routes.user.router)
