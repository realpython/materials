from datetime import datetime, timezone

from notes_manager_cursor_test.markdown_io import (
    deserialize_note,
    read_note_file,
    serialize_note,
    slugify,
    write_note_file,
)
from notes_manager_cursor_test.models import Note


def test_slugify():
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("   ") == "note"


def test_serialize_roundtrip():
    note = Note(title="My Note", body="Some body text.\n", tags=["foo", "bar"])
    text = serialize_note(note)

    assert text.startswith("---\n")
    assert "title: My Note" in text
    assert "Some body text." in text

    parsed = deserialize_note(text, created_at=note.created_at)
    assert parsed.title == note.title
    assert parsed.tags == note.tags
    assert parsed.body.strip() == note.body.strip()
    assert parsed.created_at == note.created_at


def test_deserialize_requires_frontmatter():
    try:
        deserialize_note("no frontmatter here")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for missing frontmatter")


def test_write_and_read_note_file(tmp_path):
    created_at = datetime(2024, 1, 1, tzinfo=timezone.utc)
    note = Note(
        title="Grocery List",
        body="- milk\n- eggs\n",
        tags=["home"],
        created_at=created_at,
    )

    path = write_note_file(note, tmp_path)
    assert path.exists()
    assert path.name == "grocery-list.md"

    loaded = read_note_file(path, created_at=created_at)
    assert loaded.title == note.title
    assert loaded.tags == note.tags
    assert loaded.body.strip() == note.body.strip()
