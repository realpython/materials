# How to Set Up a Python Project for Agentic Coding

This folder contains the sample code for the Real Python tutorial
[How to Set Up a Python Project for Agentic Coding](https://realpython.com/python-project-for-agentic-coding/).

It is the finished project from the tutorial: a small Python package wired up
with the automated feedback an AI coding agent needs, namely Ruff for linting
and formatting, mypy in strict mode for type checking, pytest with a coverage
gate for behavior, and pre-commit to run those checks before every commit.

## Setup

Install [uv](https://docs.astral.sh/uv/#installation), then install the
dependencies and the pre-commit hooks:

```console
$ uv sync
$ uv run pre-commit install
```

## Running the checks

Each tool can be run on its own:

```console
$ uv run ruff check .
$ uv run mypy .
$ uv run pytest
```

Or run everything the way the agent is told to in `AGENTS.md`:

```console
$ uv run pre-commit run --all-files
```

## What each file is for

| File | Purpose |
| --- | --- |
| `pyproject.toml` | Dependencies plus the Ruff, mypy, and pytest configuration |
| `AGENTS.md` | Workflow conventions an agent should follow |
| `.pre-commit-config.yaml` | Checks that run before each commit |
| `tests/` | Executable specification of the expected behavior |
| `.env.example` | Documents required environment variables without exposing secrets |
