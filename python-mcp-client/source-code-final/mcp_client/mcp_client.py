import sys
from contextlib import AsyncExitStack
from typing import Any, Awaitable, Callable, ClassVar, Self

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from mcp_client import chat
from mcp_client.handlers import OpenAIQueryHandler


class MCPClient:
    """MCP client to interact with MCP server.

    Usage:
        async with MCPClient(server_path) as client:
            # Call client methods here...
    """

    client_session: ClassVar[ClientSession]

    def __init__(self, server_path: str):
        self.server_path = server_path
        self.exit_stack = AsyncExitStack()

    async def __aenter__(self) -> Self:
        cls = type(self)
        cls.client_session = await self._connect_to_server()
        return self

    async def __aexit__(self, *_) -> None:
        await self.exit_stack.aclose()

    async def _connect_to_server(self) -> ClientSession:
        try:
            read, write = await self.exit_stack.enter_async_context(
                stdio_client(
                    server=StdioServerParameters(
                        command="sh",
                        args=[
                            "-c",
                            f"{sys.executable} {self.server_path} 2>/dev/null",
                        ],
                        env=None,
                    )
                )
            )
            client_session = await self.exit_stack.enter_async_context(
                ClientSession(read, write)
            )
            await client_session.initialize()
            return client_session
        except Exception:
            raise RuntimeError("Error: Failed to connect to server")

    async def list_all_members(self) -> None:
        """List all available tools, prompts, and resources."""
        print("MCP Server Members")
        print("=" * 50)

        sections = {
            "tools": self.client_session.list_tools,
            "prompts": self.client_session.list_prompts,
            "resources": self.client_session.list_resources,
        }
        for section, listing_method in sections.items():
            await self._list_section(section, listing_method)

        print("\n" + "=" * 50)

    async def _list_section(
        self,
        section: str,
        list_method: Callable[[], Awaitable[Any]],
    ) -> None:
        try:
            items = getattr(await list_method(), section)
            if items:
                print(f"\n{section.upper()} ({len(items)}):")
                print("-" * 30)
                for item in items:
                    description = item.description or "No description"
                    print(f" > {item.name} - {description}")
            else:
                print(f"\n{section.upper()}: None available")
        except Exception as e:
            print(f"\n{section.upper()}: Error - {e}")

    async def run_chat(self) -> None:
        """Start interactive chat with MCP server using OpenAI."""
        try:
            handler = OpenAIQueryHandler(self.client_session)
            await chat.run_chat(handler)
        except RuntimeError as e:
            print(e)
