"""
Copyright © 2025 Team Autixs. All Rights Reserved.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import os
import jwt
import time

load_dotenv()

API_KEYS = {k.strip() for k in os.getenv("API_KEYS", "").split(",") if k.strip()}
JWT_SECRET = os.getenv("JWT_SECRET", "autixs-super-secret-2025")
ALLOWED_IPS = {ip.strip() for ip in os.getenv("ALLOWED_IPS", "").split(",") if ip.strip()}

security = HTTPBearer()

async def verify_auth(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    # API Key check
    if token in API_KEYS:
        return {"type": "api_key", "key": token}

    # JWT check
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        if payload.get("exp", 0) < time.time():
            raise HTTPException(status_code=401, detail="JWT expired")
        return {"type": "jwt", "user": payload["sub"]}
    except:
        pass

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")