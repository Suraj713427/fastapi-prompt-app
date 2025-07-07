from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Prompt Backend API",
    description="Backend test using FastAPI with login, prompt, and history",
    version="1.0"
)

app.include_router(router)