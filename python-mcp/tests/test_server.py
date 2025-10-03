from contextlib import AsyncExitStack

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PATH = "/path/to/your/python-mcp/main.py"
EXPECTED_TOOLS = [
    "get_customer_info",
    "get_order_details",
    "check_inventory",
    "get_customer_ids_by_name",
    "get_orders_by_customer_id",
]


@pytest.mark.asyncio
async def test_mcp_server_connection():
    """Connect to an MCP server and verify the tools"""

    exit_stack = AsyncExitStack()

    server_params = StdioServerParameters(
        command="python", args=[SERVER_PATH], env=None
    )

    stdio_transport = await exit_stack.enter_async_context(
        stdio_client(server_params)
    )
    stdio, write = stdio_transport
    session = await exit_stack.enter_async_context(ClientSession(stdio, write))

    await session.initialize()

    response = await session.list_tools()
    tools = response.tools
    tool_names = [tool.name for tool in tools]
    tool_descriptions = [tool.description for tool in tools]

    print("\nYour server has the follow tools:")
    for tool_name, tool_description in zip(tool_names, tool_descriptions):
        print(f"{tool_name}: {tool_description}")

    assert sorted(EXPECTED_TOOLS) == sorted(tool_names)

    await exit_stack.aclose()
