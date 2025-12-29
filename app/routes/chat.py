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
from ..config import OLLAMA_HOST, DEFAULT_MODEL
from ..auth import verify_api_key

router = APIRouter()

@router.post("/v1/chat/completions")
async def chat_completions(body: dict, key: str = Depends(verify_api_key)):
    if "model" not in body:
        body["model"] = DEFAULT_MODEL
    
    response = requests.post(f"{OLLAMA_HOST}/v1/chat/completions", json=body, stream=body.get("stream", False))
    if body.get("stream", False):
        return response.iter_content(chunk_size=1024)
    return response.json()

@router.get("/v1/models")
async def list_models(key: str = Depends(verify_api_key)):
    response = requests.get(f"{OLLAMA_HOST}/v1/models")
    return response.json()