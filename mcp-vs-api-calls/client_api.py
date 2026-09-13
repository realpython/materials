import json

import anthropic
from anthropic.types import Message, ToolUseBlock

from tool import get_package_info

MODEL = "claude-sonnet-5"
QUESTION = (
    "What is the latest version of the Jinja2 package? "
    "Answer in one short plain-text sentence."
)

TOOLS = [
    {
        "name": "get_package_info",
        "description": (
            "Look up a package on PyPI and return its "
            "latest version and summary."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "package_name": {
                    "type": "string",
                    "description": "The package name on PyPI.",
                },
            },
            "required": ["package_name"],
        },
    },
]


def ask_model(
    client: anthropic.Anthropic,
    messages: list[dict],
    tools: list[dict],
    model: str = MODEL,
) -> Message:
    return client.messages.create(
        model=model,
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )


def run_tool(block: ToolUseBlock) -> str:
    result = get_package_info(**block.input)
    return json.dumps(result)


def tool_result(block: ToolUseBlock, output: str) -> dict:
    return {
        "role": "user",
        "content": [
            {
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": output,
            },
        ],
    }


def main() -> None:
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": QUESTION}]
    response = ask_model(client, messages, TOOLS)
    for block in response.content:
        if block.type == "tool_use":
            messages.append(
                {"role": "assistant", "content": response.content},
            )
            messages.append(tool_result(block, run_tool(block)))
    final = ask_model(client, messages, TOOLS)
    print(final.content[0].text)


if __name__ == "__main__":
    main()
