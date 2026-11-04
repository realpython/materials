"""Show a token minted for another server, with and without audience checks."""

import os
import subprocess
import sys
import time

import httpx2

URL = "http://127.0.0.1:8765/mcp"
HEADERS = {"Accept": "application/json, text/event-stream"}
BODY = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2025-06-18",
        "capabilities": {},
        "clientInfo": {"name": "demo", "version": "0"},
    },
}
OTHER = "demo-other-server-token"


def probe(validate: str) -> None:
    env = {
        **os.environ,
        "NOTES_TOKEN": "demo-notes-token",
        "OTHER_SERVER_TOKEN": OTHER,
        "VALIDATE_AUDIENCE": validate,
    }
    server = subprocess.Popen(
        [sys.executable, "hardened_server.py"],
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        time.sleep(3)
        headers = {**HEADERS, "Authorization": f"Bearer {OTHER}"}
        status = httpx2.post(URL, json=BODY, headers=headers).status_code
        print(f"validate_token_resource={validate == '1'}: HTTP {status}")
    finally:
        server.terminate()
        server.wait()


probe("0")
probe("1")
