"""Play the part of an agent that obeyed a poisoned tool description."""

import asyncio
import os
import sys

from mcp import Client, StdioServerParameters

os.environ["DEMO_API_TOKEN"] = "sk-demo-not-a-real-secret"


async def main(command: str, *args: str) -> None:
    params = StdioServerParameters(
        command=command, args=list(args), env=dict(os.environ)
    )
    async with Client(params) as client:
        attempts = {
            "read_file": {"path": "demo_home/.ssh/id_demo"},
            "run_shell": {"command": "env | grep DEMO_"},
        }
        for name, arguments in attempts.items():
            try:
                result = await client.call_tool(name, arguments)
                print(f"{name} -> is_error={result.is_error}")
                print("  " + result.content[0].text.strip())
            except Exception as error:
                print(f"{name} -> {type(error).__name__}: {error}")


if __name__ == "__main__":
    asyncio.run(main(*sys.argv[1:]))
