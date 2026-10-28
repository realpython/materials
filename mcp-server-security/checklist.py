"""Before/after hardening checklist: vulnerable vs hardened server."""

import asyncio
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import httpx2
from mcp import Client, StdioServerParameters
from mcp.client.streamable_http import streamable_http_client

from sandbox import sandboxed_params
from scan_server import scan_tools

HERE = Path(__file__).parent
URL = "http://127.0.0.1:8765/mcp"
HEADERS = {"Accept": "application/json, text/event-stream"}
GOOD, OTHER = "demo-notes-token", "demo-other-server-token"
BODY = {"jsonrpc": "2.0", "id": 1, "method": "ping"}


def report(check: str, before: str, after: str) -> None:
    print(f"{check:<34}{before:<12}{after}")


async def call_ok(client: Client, name: str, args: dict) -> bool:
    try:
        result = await client.call_tool(name, args)
    except Exception:
        return False
    return not result.is_error


async def output(client: Client, name: str, args: dict) -> str:
    try:
        result = await client.call_tool(name, args)
    except Exception as error:
        return f"EXC {error}"
    return result.content[0].text if result.content else ""


async def status(token: str | None) -> int:
    headers = dict(HEADERS)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    async with httpx2.AsyncClient() as http:
        return (await http.post(URL, json=BODY, headers=headers)).status_code


async def sandbox_checks() -> None:
    async with Client(sandboxed_params("vulnerable_server.py")) as boxed:
        wrote = "Read-only" not in await output(
            boxed, "run_shell", {"command": "touch /app/pwned"}
        )
        net = "unreachable" not in await output(
            boxed,
            "run_shell",
            {
                "command": 'python3 -c "import socket; '
                "socket.create_connection(('1.1.1.1', 80), timeout=3)\""
            },
        )
        seen = await call_ok(
            boxed, "read_file", {"path": "demo_home/notes.txt"}
        )
    report(
        "Sandbox: write to disk",
        "allowed",
        "allowed" if wrote else "blocked",
    )
    report(
        "Sandbox: outbound network",
        "allowed",
        "allowed" if net else "blocked",
    )
    report(
        "Sandbox: read demo_home",
        "allowed",
        "allowed" if seen else "blocked",
    )


async def main() -> None:
    os.environ["DEMO_API_TOKEN"] = "sk-demo-not-a-real-secret"
    python = sys.executable
    vuln = StdioServerParameters(
        command=python,
        args=["vulnerable_server.py"],
        env=dict(os.environ),
    )
    server_env = {
        **os.environ,
        "NOTES_TOKEN": GOOD,
        "OTHER_SERVER_TOKEN": OTHER,
    }
    server = subprocess.Popen(
        [python, "hardened_server.py"],
        env=server_env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        time.sleep(3)
        report("CHECK", "BEFORE", "AFTER")
        async with Client(vuln) as before:
            vuln_flags = await scan_tools(before, verbose=False)
            leak = "sk-demo" in await output(
                before, "run_shell", {"command": "echo $DEMO_API_TOKEN"}
            )
            read_any = await call_ok(
                before, "read_file", {"path": "demo_home/.ssh/id_demo"}
            )
            shell = await call_ok(before, "run_shell", {"command": "id"})
        http = httpx2.AsyncClient(headers={"Authorization": f"Bearer {GOOD}"})
        async with Client(
            streamable_http_client(URL, http_client=http)
        ) as after:
            hard_flags = await scan_tools(after, verbose=False)
            escape = await call_ok(
                after, "read_note", {"name": "../demo_home/notes.txt"}
            )
            tools = {tool.name for tool in (await after.list_tools()).tools}
        report(
            "Tool metadata scanner findings", str(vuln_flags), str(hard_flags)
        )
        report(
            "Arbitrary shell tool",
            "exposed" if shell else "-",
            "exposed" if "run_shell" in tools else "removed",
        )
        report(
            "Read outside allowed folder",
            "allowed" if read_any else "blocked",
            "allowed" if escape else "blocked",
        )
        report(
            "Secret visible to tools", "leaked" if leak else "hidden", "n/a"
        )
        report(
            "No token -> HTTP status", "n/a (stdio)", str(await status(None))
        )
        report(
            "Other server's token -> status",
            "n/a (stdio)",
            str(await status(OTHER)),
        )
        report("Own token -> MCP session", "n/a (stdio)", "connected")
        if shutil.which("bwrap") is None:
            for check in (
                "write to disk",
                "outbound network",
                "read demo_home",
            ):
                report(f"Sandbox: {check}", "allowed", "skipped")
            return
        await sandbox_checks()
    finally:
        server.terminate()


asyncio.run(main())
