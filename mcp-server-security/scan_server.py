"""Connect to a server as a client would and flag risky tool metadata."""

import asyncio
import re
import sys

from mcp import Client, StdioServerParameters

SUSPICIOUS = {
    "hidden instruction tag": re.compile(
        r"<\s*(important|system|instructions?)\s*>", re.I
    ),
    "secrecy request": re.compile(r"do not (mention|tell|reveal)", re.I),
    "sensitive path": re.compile(r"\.ssh|\.env|id_rsa|credentials", re.I),
    "cross-tool call": re.compile(r"\bcall\s+\w+\s+on\b", re.I),
}
BROAD_NAMES = re.compile(r"shell|exec|eval|sudo|any file", re.I)


async def scan_tools(client: Client, verbose: bool = True) -> int:
    findings = 0
    result = await client.list_tools()
    for tool in result.tools:
        description = tool.description or ""
        if verbose:
            print(f"tool: {tool.name}")
            print(f"  description: {description!r}")
        for label, pattern in SUSPICIOUS.items():
            if pattern.search(description):
                if verbose:
                    print(f"  FLAG {label}")
                findings += 1
        if BROAD_NAMES.search(f"{tool.name} {description}"):
            if verbose:
                print("  FLAG over-broad capability")
            findings += 1
    return findings


async def scan(command: str, *args: str) -> int:
    params = StdioServerParameters(command=command, args=list(args))
    async with Client(params) as client:
        findings = await scan_tools(client)
    print(f"{findings} finding(s)")
    return findings


if __name__ == "__main__":
    sys.exit(1 if asyncio.run(scan(*sys.argv[1:])) else 0)
