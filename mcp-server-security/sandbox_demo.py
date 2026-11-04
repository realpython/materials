"""Run the vulnerable server's own tools inside the sandbox."""

import asyncio
import os

from mcp import Client

from sandbox import sandboxed_params

os.environ["DEMO_API_TOKEN"] = "sk-demo-not-a-real-secret"

CALLS = [
    ("read_file", {"path": "demo_home/.ssh/id_demo"}),
    ("read_file", {"path": "workspace/notes.txt"}),
    ("run_shell", {"command": "env | grep DEMO_ || echo no DEMO_ vars"}),
    ("run_shell", {"command": "touch /app/pwned && echo wrote"}),
    (
        "run_shell",
        {
            "command": 'python3 -c "import socket; '
            "socket.create_connection(('1.1.1.1', 80), timeout=3)\""
        },
    ),
    ("run_shell", {"command": "id -u; ls /home"}),
]


async def main() -> None:
    async with Client(sandboxed_params("vulnerable_server.py")) as client:
        for name, arguments in CALLS:
            result = await client.call_tool(name, arguments)
            text = result.content[0].text.strip().splitlines()
            print(f"{name} {arguments}")
            print("  ->", " | ".join(text) or "(empty)")


asyncio.run(main())
