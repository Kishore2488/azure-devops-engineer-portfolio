"""Small Microsoft Fabric REST client skeleton.

Set FABRIC_API_BASE, FABRIC_TOKEN and FABRIC_WORKSPACE_ID in the environment.
The token is never stored in source control.
"""
import os
import requests

BASE = os.environ["FABRIC_API_BASE"].rstrip("/")
TOKEN = os.environ["FABRIC_TOKEN"]
WORKSPACE = os.environ["FABRIC_WORKSPACE_ID"]

def workspace():
    response = requests.get(
        f"{BASE}/workspaces/{WORKSPACE}",
        headers={"Authorization": f"Bearer {TOKEN}"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print(workspace())
