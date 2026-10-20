# AI Agent Memory in Python: A Primer

This folder contains the sample code for the Real Python tutorial [AI Agent Memory in Python: A Primer](https://realpython.com/ai-agent-memory/).

## Setup

Both scripts call the OpenAI API, so they need an `OPENAI_API_KEY` and make paid API calls:

```console
$ export OPENAI_API_KEY="your-api-key"
```

Each script declares its dependency, `openai==3.35.1`, in an inline script metadata block, so [uv](https://docs.astral.sh/uv/) installs it for you. If you don't use uv, install the pinned package with `python -m pip install openai==3.35.1` and run the scripts with `python`.

## Short-Term Memory

`short_term.py` asks the same question with and without the conversation history:

```console
$ uv run short_term.py
```

## Self-Managed Long-Term Memory

`long_term.py` gives the model four memory tools and stores what it saves in `memories.json`. Each command is a fresh session, so the agent remembers only what's in the file. Delete `memories.json` to start over.

Here's the full five-message run from the tutorial. The model's wording, its memories, and even its choice of tools vary from run to run:

```console
$ uv run long_term.py "Hi! I'm Ana, I'm learning Python, and I prefer short answers with code examples."
  tool: save_memory({'text': 'User name is Ana. She is learning Python and prefers short answers with code examples.'})
Hi Ana! I’ll keep answers short and include code examples.
$ uv run long_term.py "I moved from Lisbon to Berlin last month."
  tool: save_memory({'text': 'User moved from Lisbon to Berlin last month.'})
Got it.
$ uv run long_term.py "Forget that I prefer short answers."
  tool: search_memory({'query': 'prefer short answers'})
  tool: update_memory({'id': '1', 'text': 'User name is Ana. She is learning Python and no longer prefers short answers.'})
Got it — I’ve removed the short-answer preference.
$ uv run long_term.py "Where do I live, and what do you know about me?"
  tool: search_memory({'query': 'user personal facts location preferences bio'})
I know that you’re Ana, you’re learning Python, and you moved from Lisbon to Berlin last month.

So, you likely live in Berlin now.
$ uv run long_term.py "What's the capital of France?"
The capital of France is Paris.
```

After this run, `memories.json` holds two entries:

```json
{
  "1": "User name is Ana. She is learning Python and no longer prefers short answers.",
  "2": "User moved from Lisbon to Berlin last month."
}
```
