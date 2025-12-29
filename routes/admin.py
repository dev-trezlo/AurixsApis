"""
Copyright © 2025 Team Autixs. All Rights Reserved.
Private Use Only – Team Autixs Exclusive.
"""

from fastapi import APIRouter, Depends, HTTPException
from security.auth import verify_auth
from dotenv import load_dotenv
import os
import subprocess
import json

load_dotenv()
ADMIN_KEYS = {k.strip() for k in os.getenv("ADMIN_KEYS", "").split(",") if k.strip()}  # Alag keys admin ke liye

router = APIRouter()

def verify_admin(auth = Depends(verify_auth)):
    if auth.get("type") == "api_key" and auth.get("key") not in ADMIN_KEYS:
        raise HTTPException(status_code=403, detail="Admin access denied – not god key")
    return auth

@router.get("/stats")
async def api_stats(admin = Depends(verify_admin)):
    # Logs se usage count kar ya simple stats
    return {"status": "god mode", "message": "Team Autixs admin panel", "active_models": subprocess.getoutput("ollama list")}

@router.post("/pull-model")
async def pull_new_model(body: dict, admin = Depends(verify_admin)):
    model = body.get("model")
    if not model:
        raise HTTPException(400, detail="model name required")
    result = subprocess.getoutput(f"ollama pull {model}")
    return {"pulled": model, "output": result}

@router.post("/generate-key")
async def generate_new_key(body: dict, admin = Depends(verify_admin)):
    new_key = f"sk-autixs-{os.urandom(16).hex()}"
    # .env mein append kar (real mein file write kar)
    with open(".env", "a") as f:
        f.write(f"\nAPI_KEYS+={new_key}")
    return {"new_api_key": new_key, "message": "Fresh key generated – share with team only"}

@router.get("/logs")
async def view_logs(admin = Depends(verify_admin)):
    logs = subprocess.getoutput("tail -50 api.log")
    return {"logs": logs.split("\n")}

@router.post("/restart")
async def restart_api(admin = Depends(verify_admin)):
    subprocess.Popen(["pkill", "uvicorn"])
    subprocess.Popen(["nohup", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", ">", "api.log", "2>&1", "&"])
    return {"message": "API restarted – darkness reloaded"}