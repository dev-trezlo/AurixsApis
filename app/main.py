from fastapi import FastAPI
from .routes.chat import router as chat_router

app = FastAPI(title="Team Arsh Uncensored AI API", version="2025")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "alive", "message": "Team Aurixs Uncensored API running – no limits, no filters"}