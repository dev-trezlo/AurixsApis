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
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .config import API_KEYS

security = HTTPBearer()

def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials not in API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
    return credentials.credentials