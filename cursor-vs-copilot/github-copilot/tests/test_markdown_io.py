from datetime import datetime

import pytest

from notes_manager_copilot_test.markdown_io import (
    note_from_markdown,
    note_to_markdown,
)
from notes_manager_copilot_test.models import Note


def test_round_trip():
    note = Note(
        title="My Note",
        body="Some body text.\n",
        tags=["work", "ideas"],
        created_at=datetime(2024, 1, 1, 12, 30),
    )
    markdown = note_to_markdown(note)
    parsed = note_from_markdown(markdown)

    assert parsed.title == note.title
    assert parsed.body == note.body
    assert parsed.tags == note.tags
    assert parsed.created_at == note.created_at


def test_note_to_markdown_contains_frontmatter():
    note = Note(
        title="T", body="B", tags=["x"], created_at=datetime(2024, 1, 1)
    )
    markdown = note_to_markdown(note)
    assert markdown.startswith("---\n")
    assert "title: T" in markdown
    assert "tags:" in markdown


def test_note_from_markdown_missing_frontmatter_raises():
    with pytest.raises(ValueError):
        note_from_markdown("no frontmatter here")
