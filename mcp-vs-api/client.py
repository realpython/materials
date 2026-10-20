import asyncio
import sys

import anthropic
from anthropic.types import Message, ToolUseBlock
from mcp import Client, StdioServerParameters

MODEL = "claude-sonnet-5"
QUESTION = (
    "What is the latest version of the Jinja2 package? "
    "Answer in one short plain-text sentence."
)


async def discover_tools(client: Client) -> list[dict]:
    discovered = await client.list_tools()
    return [
        {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.input_schema,
        }
        for tool in discovered.tools
    ]


def ask_model(
    client: anthropic.Anthropic,
    messages: list[dict],
    tools: list[dict],
    model: str = MODEL,
) -> Message:
    return client.messages.create(
        model=model,
        max_tokens=2048,
        tools=tools,
        messages=messages,
    )


async def run_tool(client: Client, block: ToolUseBlock) -> str:
    result = await client.call_tool(block.name, block.input)
    return result.content[0].text


def tool_result(block: ToolUseBlock, output: str) -> dict:
    return {
        "type": "tool_result",
        "tool_use_id": block.id,
        "content": output,
    }


async def main(server: StdioServerParameters) -> None:
    async with Client(server) as mcp:
        tools = await discover_tools(mcp)

        client = anthropic.Anthropic()
        messages = [{"role": "user", "content": QUESTION}]
        response = ask_model(client, messages, tools)

        tool_uses = [b for b in response.content if b.type == "tool_use"]
        if tool_uses:
            messages.append({"role": "assistant", "content": response.content})
            results = [
                tool_result(b, await run_tool(mcp, b)) for b in tool_uses
            ]
            messages.append({"role": "user", "content": results})

        final = ask_model(client, messages, tools)
        print(next(b.text for b in final.content if b.type == "text"))


if __name__ == "__main__":
    server = StdioServerParameters(
        command=sys.executable,
        args=["server.py"],
    )
    asyncio.run(main(server))
