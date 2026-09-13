from datetime import datetime

from notes_manager_copilot_test.models import Note


def test_note_defaults():
    note = Note(title="Title", body="Body")
    assert note.title == "Title"
    assert note.body == "Body"
    assert note.tags == []
    assert isinstance(note.created_at, datetime)


def test_note_explicit_fields():
    created_at = datetime(2024, 1, 1)
    note = Note(
        title="Title", body="Body", tags=["a", "b"], created_at=created_at
    )
    assert note.tags == ["a", "b"]
    assert note.created_at == created_at
