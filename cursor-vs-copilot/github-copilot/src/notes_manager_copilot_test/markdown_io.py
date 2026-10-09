"""Serialize and parse notes as Markdown files with YAML frontmatter."""

from datetime import datetime

import yaml

from .models import Note

FRONTMATTER_DELIMITER = "---"


def note_to_markdown(note: Note) -> str:
    """Render a note as Markdown text with a YAML frontmatter header."""
    frontmatter = {
        "title": note.title,
        "tags": note.tags,
        "created_at": note.created_at.isoformat(),
    }
    frontmatter_text = yaml.safe_dump(frontmatter, sort_keys=False)
    return f"{FRONTMATTER_DELIMITER}\n{frontmatter_text}{FRONTMATTER_DELIMITER}\n{note.body}"


def note_from_markdown(text: str) -> Note:
    """Parse Markdown text with a YAML frontmatter header into a note."""
    if not text.startswith(f"{FRONTMATTER_DELIMITER}\n"):
        raise ValueError("Markdown text is missing a YAML frontmatter header")

    _, frontmatter_text, body = text.split(FRONTMATTER_DELIMITER, 2)
    frontmatter = yaml.safe_load(frontmatter_text) or {}

    title = frontmatter.get("title", "")
    tags = list(frontmatter.get("tags") or [])
    created_at_raw = frontmatter.get("created_at")
    created_at = (
        datetime.fromisoformat(created_at_raw)
        if created_at_raw
        else datetime.utcnow()
    )

    return Note(
        title=title, body=body.lstrip("\n"), tags=tags, created_at=created_at
    )
