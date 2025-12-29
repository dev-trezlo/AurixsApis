#!/bin/bash
# Copyright © 2025 Team Autixs. All Rights Reserved.
# Private Use Only – Unauthorized distribution prohibited.
# Team Autixs Exclusive Property.
echo "Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

echo "Starting Ollama service..."
sudo systemctl start ollama

echo "Pulling uncensored beasts..."
ollama pull dolphin-llama3.1:8b
ollama pull dolphin-mixtral:8x7b
ollama pull wizardlm-uncensored

echo "Installing Python deps..."
pip install fastapi uvicorn python-dotenv requests pydantic

echo "API ready. Run: uvicorn app.main:app --host 0.0.0.0 --port 8000"