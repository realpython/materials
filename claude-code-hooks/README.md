# Claude Code Hooks Demo

Supporting materials for the Real Python tutorial **How to Automate Your Workflow With Claude Code Hooks**.

This is a small [uv](https://docs.astral.sh/uv/)-managed project with three Claude Code hooks wired up in `.claude/`:

- **`Stop` hook** (`notify_desktop.py`): a desktop notification each time Claude finishes responding (macOS and Linux; plain-text fallback on other systems).
- **`PreToolUse` hook** (`guard_pip.py`): blocks `pip install` and steers Claude toward `uv`.
- **`PostToolUse` hook** (`format_with_ruff.py`): formats the file Claude just edited with ruff.

Each hook is a small Python script in `.claude/hooks/`, wired up in `settings.json`.

## Setup

You need Python 3.12 or later, uv, and ruff. Install ruff as a uv tool so the hook can call it from anywhere:

```console
$ uv tool install ruff
```

Then sync the project:

```console
$ uv sync
```

## Try the hooks

Start Claude Code in this folder:

```console
$ claude
```

Then:

- Ask Claude to do anything, and you get a desktop notification when it finishes.
- Ask Claude to `pip install requests`. The hook blocks pip, and Claude uses `uv add` instead.
- Ask Claude to edit a Python file. ruff reformats the file on save.

Run `/hooks` inside Claude Code to list the wired hooks, or start with `claude --debug` to watch them fire.
