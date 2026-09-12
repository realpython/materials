# Notes Manager

A simple command-line Markdown note manager. Each note is stored twice:

- as a **Markdown file** (with YAML frontmatter) in a notes directory — the canonical, human-editable copy.
- as a row in a **SQLite index** (`notes.db`) — used for fast search and listing.

## Install

```bash
pip install -e .
```

This installs the `notes` command (entry point defined in `pyproject.toml`).

## Usage

```bash
notes [--notes-dir DIR] [--db PATH] <command> [args]
```

`--notes-dir` (default `notes/`) and `--db` (default `notes.db`) let you point at a different notes store.

### Commands

| Command | Description |
|---|---|
| `notes add <title> [--tags a,b] [--body TEXT \| --body-file PATH]` | Create or update a note (body read from `--body`, `--body-file`, or stdin). |
| `notes get <title>` | Print a note by its exact title. |
| `notes list` | List all notes, most recently created first. |
| `notes search <query>` | Search notes whose title or body contains `query` (case-insensitive). |
| `notes list-tag <tag>` | List notes with a given tag (case-insensitive, exact tag match). |
| `notes reindex` | Rebuild the SQLite index from the Markdown files on disk (fixes drift if the index and files get out of sync). |

### Examples

```bash
notes add "Git Rebase vs Merge" --tags git,vcs --body "Rebase rewrites history; merge preserves it."
notes search rebase
notes list-tag git
notes get "Git Rebase vs Merge"
```

## Notes on storage

- Titles are unique; adding a note with an existing title updates (upserts) it.
- `search` and `list-tag` query the SQLite index only. If a Markdown file is added/edited outside the CLI (or the index gets out of sync), run `notes reindex`.
- The `notes/` directory and `notes.db` hold your actual note data and are gitignored — they aren't meant to be committed to source control.

## Development

```bash
pip install -e .
pytest
```
