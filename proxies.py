"""
Copyright © 2025 Team Autixs. All Rights Reserved.
Private Use Only – Team Autixs Exclusive.
"""

import random
import httpx

PROXIES = []
with open("utils/proxies_list.txt", "r") as f:
    PROXIES = [line.strip() for line in f if line.strip()]

def get_random_proxy():
    if not PROXIES:
        return None
    return random.choice(PROXIES)

def get_httpx_client():
    proxy = get_random_proxy()
    transport = httpx.HTTPTransport(proxy=proxy) if proxy else None
    return httpx.Client(transport=transport, timeout=30.0)