"""A small helpdesk agent for internal Python packages."""

import json
import os
import sys
from pathlib import Path

from openai import OpenAI

from tools import TOOLS, call_tool

MODEL = os.environ.get("AGENT_MODEL", "gpt-5.4-mini-2026-03-17")
MAX_TURNS = 6
client = OpenAI()


def run_agent(question: str, instructions: str) -> list[dict]:
    """Run the agent loop and return the full message history."""
    messages = [
        {"role": "system", "content": instructions},
        {"role": "user", "content": question},
    ]
    for _ in range(MAX_TURNS):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
        )
        message = response.choices[0].message
        messages.append(message.to_dict())
        if not message.tool_calls:
            break
        for call in message.tool_calls:
            arguments = json.loads(call.function.arguments)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": call_tool(call.function.name, arguments),
                }
            )
    return messages


if __name__ == "__main__":
    prompt = Path("prompts/helpdesk_v1.txt").read_text()
    history = run_agent(sys.argv[1], prompt)
    print(history[-1]["content"])
