import json
from pathlib import Path

from openai import OpenAI

client = OpenAI()
MODEL = "gpt-6-luna"


def list_files(folder):
    return "\n".join(path.name for path in Path(folder).iterdir())


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List the files in a folder.",
            "parameters": {
                "type": "object",
                "properties": {"folder": {"type": "string"}},
                "required": ["folder"],
            },
        },
    },
]


def trace(sender, receiver, text):
    print(f"  [{sender} -> {receiver}] {text}")


def ask_model(messages):
    trace("harness", "model", f"sending {len(messages)} message(s)")
    response = client.chat.completions.create(
        model=MODEL,
        tools=TOOLS,
        messages=messages,
        reasoning_effort="none",
    )
    reply = response.choices[0].message
    messages.append(reply)

    for call in reply.tool_calls or []:
        trace(
            "model",
            "harness",
            f"please run {call.function.name}{call.function.arguments}",
        )
    if reply.content:
        trace(
            "model",
            "harness",
            f"text reply ({len(reply.content)} characters)",
        )

    return reply


def run_tool(call):
    args = json.loads(call.function.arguments)
    trace("harness", "tool", f"{call.function.name}({args})")
    result = list_files(**args)
    trace("tool", "harness", f"{len(result)} characters")
    return result


messages = []

while True:
    user_input = input("you -> harness: ")
    messages.append({"role": "user", "content": user_input})
    reply = ask_model(messages)

    if reply.tool_calls:
        for call in reply.tool_calls:
            result = run_tool(call)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result,
                },
            )

        reply = ask_model(messages)

    print(f"harness -> you: {reply.content}")
