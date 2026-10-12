"""Minimal Microsoft Fabric REST API client.
Provide runtime values through environment variables; never commit tokens.
"""
import os
import requests

BASE = os.environ.get("FABRIC_API_BASE", "https://api.fabric.microsoft.com/v1").rstrip("/")
TOKEN = os.environ["FABRIC_TOKEN"]
WORKSPACE_ID = os.environ["FABRIC_WORKSPACE_ID"]

def get_workspace():
    response = requests.get(
        f"{BASE}/workspaces/{WORKSPACE_ID}",
        headers={"Authorization": f"Bearer {TOKEN}"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print(get_workspace())
