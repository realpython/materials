"""Read and write notes as Markdown files with YAML frontmatter.

The on-disk format looks like::

    ---
    title: My Note
    tags:
      - foo
      - bar
    ---
    The body of the note goes here.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from .models import Note

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n?(.*)\Z", re.DOTALL)


def slugify(title: str) -> str:
    """Turn a note title into a filesystem-friendly slug."""
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.strip().lower()).strip("-")
    return slug or "note"


def serialize_note(note: Note) -> str:
    """Render a Note as Markdown text with YAML frontmatter."""
    frontmatter = yaml.safe_dump(
        {"title": note.title, "tags": list(note.tags)},
        sort_keys=False,
    )
    return f"---\n{frontmatter}---\n{note.body}"


def deserialize_note(text: str, *, created_at=None) -> Note:
    """Parse Markdown text with YAML frontmatter into a Note.

    ``created_at`` is not stored in the frontmatter (only title and tags
    are), so it must be supplied by the caller (e.g. from a database
    record or the file's modification time). If omitted, the Note's
    default (the current time) is used.
    """
    match = _FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("Note text is missing YAML frontmatter")

    raw_frontmatter, body = match.groups()
    metadata = yaml.safe_load(raw_frontmatter) or {}

    title = metadata.get("title", "")
    tags = list(metadata.get("tags") or [])
    body = body.lstrip("\n")

    kwargs = {"title": title, "body": body, "tags": tags}
    if created_at is not None:
        kwargs["created_at"] = created_at
    return Note(**kwargs)


def write_note_file(note: Note, directory: Path) -> Path:
    """Write ``note`` to a Markdown file inside ``directory`` and return its path."""
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{slugify(note.title)}.md"
    path.write_text(serialize_note(note), encoding="utf-8")
    return path


def read_note_file(path: Path, *, created_at=None) -> Note:
    """Read a Note from a Markdown file on disk."""
    return deserialize_note(
        path.read_text(encoding="utf-8"), created_at=created_at
    )
