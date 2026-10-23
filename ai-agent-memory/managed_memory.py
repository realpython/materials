# /// script
# requires-python = ">=3.11"
# dependencies = ["openai==3.35.1"]
# ///
import json
import re
import sys
from pathlib import Path

from openai import OpenAI

client = OpenAI()
MODEL = "gpt-5.4-mini"
STORE = Path("memories.json")
memories = json.loads(STORE.read_text()) if STORE.exists() else {}


def save_memory(text, tags):
    new_id = str(max(map(int, memories), default=0) + 1)
    memories[new_id] = {"text": text, "tags": _parse_tags(tags)}
    return "saved"


def _parse_tags(tags):
    return sorted(
        {tag.strip().lower() for tag in tags.split(",") if tag.strip()}
    )


def search_memory(query):
    query_words = _words(query)
    matches = {
        id: memory
        for id, memory in memories.items()
        if query_words
        & (_words(memory["text"]) | _words(" ".join(memory["tags"])))
    }
    return json.dumps(matches)


STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "do",
    "i",
    "is",
    "me",
    "my",
    "of",
    "the",
    "to",
    "user",
    "what",
    "where",
}


def _words(text):
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOP_WORDS


def update_memory(id, text, tags):
    if id not in memories:
        return "not found"
    memories[id] = {"text": text, "tags": _parse_tags(tags)}
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
    spec(
        save_memory,
        "Store a fact with comma-separated topic tags.",
        "text",
        "tags",
    ),
    spec(
        search_memory,
        "Search memories by topic or keywords, such as location or preferences.",
        "query",
    ),
    spec(
        update_memory,
        "Replace a memory and its comma-separated tags.",
        "id",
        "text",
        "tags",
    ),
    spec(delete_memory, "Delete a wrong or unneeded memory.", "id"),
]

if len(sys.argv) != 2:
    sys.exit('Usage: uv run managed_memory.py "Your message"')

messages = [
    {
        "role": "system",
        "content": "You have tools to manage your own long-term memory. Decide "
        "when to save, search, update, or delete memories. Give each memory "
        "topic tags, such as location or preferences. Search by topic first "
        "to get ids before you update or delete. Answer briefly.",
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
