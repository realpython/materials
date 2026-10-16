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


messages = []

while True:
    user_input = input("you -> harness: ")
    messages.append({"role": "user", "content": user_input})

    trace("harness", "model", f"sending {len(messages)} message(s)")
    response = client.chat.completions.create(
        model=MODEL,
        tools=TOOLS,
        messages=messages,
        reasoning_effort="none",
    )
    reply = response.choices[0].message
    messages.append(reply)
    # trace("model", "harness", f"text reply ({len(reply.content)} characters)")
    print(reply.tool_calls)

    print(f"harness -> you: {reply.content}")
