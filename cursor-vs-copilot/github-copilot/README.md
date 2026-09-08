# Notes Manager

A CLI for managing Markdown notes, backed by a SQLite database.

## Install

```bash
pip install -e .
```

## Usage

```
notes [--db PATH] <command> [args]
```

`--db` sets the SQLite database path (default: `~/.notes-manager-copilot-test/notes.db`).

| Command | Description |
|---|---|
| `notes add <title> <body> [--tags TAG ...]` | Create a note |
| `notes get <title>` | Fetch a note by exact title |
| `notes search <query>` | Find notes whose title or body contains `query` |
| `notes list-tag <tag>` | List notes with a given tag |

## Storage

- Notes are stored in a SQLite database at the `--db` path.
- Each note added via `add` is also written as a Markdown file (with YAML frontmatter for `title`, `tags`, `created_at`) to a `notes/` folder next to the database.

## Development

```bash
pip install -e ".[dev]"
pytest
```
