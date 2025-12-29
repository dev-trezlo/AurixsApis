"""
Copyright © 2025 Team Autixs. All Rights Reserved.
Private Use Only – Team Autixs Exclusive.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware
from security.rate_limiter import limiter
from routes import chat, models, admin
from utils.logger import setup_logger

app = FastAPI(
    title="Team Autixs Uncensored API 2025",
    description="Zero limits. Zero filters. Pure abyss.",
    version="2.0"
)


app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.limiter = limiter
setup_logger()

# Routes
app.include_router(chat.router, prefix="/v1")
app.include_router(models.router, prefix="/v1")
app.include_router(admin.router, prefix="/admin")   

@app.get("/")
def root():
    return {"status": "alive", "message": "Team Autixs Uncensored API – no limits, no morals"}