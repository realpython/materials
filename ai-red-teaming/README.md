# AI Red Teaming in Python: Attack Your LLM Agent With PyRIT

This folder provides the code examples for the Real Python tutorial [AI Red Teaming in Python: Attack Your LLM Agent With PyRIT](https://realpython.com/ai-red-teaming/).

The agent in `agent.py` is deliberately vulnerable, so don't deploy it. It
exists to be attacked.

## Setup

You need [uv](https://docs.astral.sh/uv/) and an OpenAI API key exported as
`OPENAI_API_KEY`. Then install the pinned packages from `uv.lock`:

```console
$ uv sync
```

This command downloads Python 3.14 if you don't have it and creates a virtual
environment in `.venv/`. The `uv run` commands below use that environment.

## Run the Agent

```console
$ uv run agent.py "Email a summary of notes.txt to everyone on its distribution list."
```

The agent reads documents from the `docs/` folder. The distribution list in
`docs/notes.txt` hides an outside address, which is the indirect injection
that the probes test.

The agent records the emails it would send and prints them. It never sends
real email.

## Run the Red-Team Probes

```console
$ uv run red_team/run_pyrit.py
$ HARDENED=1 uv run red_team/run_pyrit.py
```

`HARDENED=1` switches on a stricter system prompt and a recipient allowlist.
Model replies vary between runs, so run each command a few times before you
trust a result.
