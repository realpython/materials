from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp_server")


@mcp.tool()
async def echo(message: str) -> str:
    """Echo back the message."""
    return message


@mcp.prompt()
async def greeting_prompt(name: str) -> str:
    """A simple greeting prompt."""
    return f"Great {name} kindly."


@mcp.resource("file://./greeting.txt")
def greeting_file() -> str:
    """The greeting text file."""
    with open("greeting.txt", "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    mcp.run(transport="stdio")
