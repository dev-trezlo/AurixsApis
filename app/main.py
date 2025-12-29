"""
Copyright © 2025 Team Autixs. All Rights Reserved.

This code is the exclusive property of Team Autixs.
Unauthorized copying, distribution, modification, reverse engineering,
public disclosure, or use of this code in any form is strictly prohibited.

No part of this repository may be reproduced, stored in a retrieval system,
or transmitted without prior written permission from Team Autixs.

Violators will be hunted down in the digital abyss.

Private Use Only – Team Autixs Members Exclusive.
"""
from fastapi import FastAPI
from .routes.chat import router as chat_router

app = FastAPI(title="Team Arsh Uncensored AI API", version="2025")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "alive", "message": "Uncensored API running – no limits, no filters"}