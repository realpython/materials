from pathlib import Path

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("mcp_server")


@mcp.tool()
async def echo(message: str) -> str:
    """Echo back the message."""
    return message


@mcp.prompt()
async def greeting_prompt(name: str) -> str:
    """A simple greeting prompt."""
    return f"Greet {name} kindly."


@mcp.resource("file://./greeting.txt")
def greeting_file() -> str:
    """The greeting text file."""
    path = Path(__file__).parent / "greeting.txt"
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    mcp.run(transport="stdio")
