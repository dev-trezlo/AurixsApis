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
from fastapi import APIRouter, Depends
import requests
from proxies import get_httpx_client
from security.auth import verify_auth
from dotenv import load_dotenv
import os

load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")

router = APIRouter()

@router.post("/chat/completions")
async def chat_completions(body: dict, auth = Depends(verify_auth)):
    body["model"] = body.get("model", os.getenv("DEFAULT_MODEL"))
    
    # Outgoing Ollama call (local hai to direct, future mein remote bhi)
    response = requests.post(f"{OLLAMA_HOST}/v1/chat/completions", json=body, stream=body.get("stream", False))
    
    if body.get("stream", False):
        return response.iter_content(chunk_size=1024)
    return response.json()