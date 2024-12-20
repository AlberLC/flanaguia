from fastapi import FastAPI

import routes.question
import routes.user

app = FastAPI()

app.include_router(projects.api_kahoot.routes.question.router)
app.include_router(projects.api_kahoot.routes.user.router)
