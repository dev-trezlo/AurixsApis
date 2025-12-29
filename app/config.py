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
from dotenv import load_dotenv
import os

load_dotenv()

API_KEYS = os.getenv("API_KEYS", "test").split(",")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "dolphin-llama3.1:8b")