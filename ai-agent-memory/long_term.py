# /// script
# requires-python = ">=3.11"
# dependencies = ["openai==3.35.1"]
# ///
import json
import sys
from pathlib import Path

from openai import OpenAI

client = OpenAI()
MODEL = "gpt-5.4-mini"
STORE = Path("memories.json")
memories = json.loads(STORE.read_text()) if STORE.exists() else {}


def save_memory(text):
    memories[str(max(map(int, memories), default=0) + 1)] = text
    return "saved"


def search_memory(query):
    return json.dumps(memories)  # Tiny store: return everything


def update_memory(id, text):
    if id not in memories:
        return "not found"
    memories[id] = text
    return "updated"


def delete_memory(id):
    if id not in memories:
        return "not found"
    del memories[id]
    return "deleted"


def spec(fn, description, *params):
    props = {name: {"type": "string"} for name in params}
    schema = {
        "type": "object",
        "properties": props,
        "required": list(params),
        "additionalProperties": False,
    }
    return {
        "type": "function",
        "function": {
            "name": fn.__name__,
            "description": description,
            "parameters": schema,
            "strict": True,
        },
    }


TOOLS = {
    f.__name__: f
    for f in (save_memory, search_memory, update_memory, delete_memory)
}
SPECS = [
    spec(save_memory, "Store a durable fact about the user.", "text"),
    spec(search_memory, "Read the stored memories.", "query"),
    spec(update_memory, "Replace an outdated memory.", "id", "text"),
    spec(delete_memory, "Delete a wrong or unneeded memory.", "id"),
]

if len(sys.argv) != 2:
    sys.exit('Usage: uv run long_term.py "Your message"')

messages = [
    {
        "role": "system",
        "content": "You have long-term memory tools. Decide yourself "
        "when to save, search, update, or delete memories. Search first to get "
        "ids before you update or delete. Answer briefly.",
    },
    {"role": "user", "content": sys.argv[1]},
]
for _ in range(10):  # The agent loop, capped at ten rounds
    reply = (
        client.chat.completions.create(
            model=MODEL, messages=messages, tools=SPECS
        )
        .choices[0]
        .message
    )
    messages.append(reply)
    if not reply.tool_calls:
        break
    for call in reply.tool_calls:
        args = json.loads(call.function.arguments)
        print(f"  tool: {call.function.name}({args})")
        result = TOOLS[call.function.name](**args)
        STORE.write_text(json.dumps(memories, indent=2))  # Save every change
        messages.append(
            {"role": "tool", "tool_call_id": call.id, "content": result}
        )
print(reply.content)
