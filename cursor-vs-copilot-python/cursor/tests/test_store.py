import pytest

from notes_manager_cursor_test.models import Note
from notes_manager_cursor_test.store import NoteStore


@pytest.fixture
def store(tmp_path):
    with NoteStore(tmp_path / "notes", tmp_path / "notes.db") as store:
        yield store


def test_add_and_get_note(store):
    note = Note(
        title="Recipe", body="Mix flour and water.", tags=["cooking", "bread"]
    )
    store.add_note(note)

    fetched = store.find_note_by_title("Recipe")
    assert fetched is not None
    assert fetched.title == "Recipe"
    assert fetched.body == "Mix flour and water."
    assert set(fetched.tags) == {"cooking", "bread"}


def test_get_missing_note_returns_none(store):
    assert store.find_note_by_title("Nonexistent") is None


def test_add_note_writes_markdown_file(store):
    note = Note(title="Shopping", body="- bread\n- butter", tags=["home"])
    store.add_note(note)

    files = list(store.notes_dir.glob("*.md"))
    assert len(files) == 1
    assert "title: Shopping" in files[0].read_text()


def test_search_notes_matches_title_and_body(store):
    store.add_note(
        Note(title="Trip Plan", body="Visit the mountains", tags=["travel"])
    )
    store.add_note(
        Note(title="Work Notes", body="Discuss trip budget", tags=["work"])
    )
    store.add_note(
        Note(title="Unrelated", body="Nothing to see here", tags=[])
    )

    results = store.find_notes_by_title_and_body("trip")
    titles = {note.title for note in results}
    assert titles == {"Trip Plan", "Work Notes"}


def test_list_notes_by_tag(store):
    store.add_note(Note(title="Note A", body="a", tags=["red", "blue"]))
    store.add_note(Note(title="Note B", body="b", tags=["blue"]))
    store.add_note(Note(title="Note C", body="c", tags=["green"]))

    results = store.find_notes_by_tag("blue")
    titles = {note.title for note in results}
    assert titles == {"Note A", "Note B"}

    assert store.find_notes_by_tag("purple") == []


def test_add_note_upserts_on_same_title(store):
    store.add_note(Note(title="Duplicate", body="first version", tags=["v1"]))
    store.add_note(Note(title="Duplicate", body="second version", tags=["v2"]))

    fetched = store.find_note_by_title("Duplicate")
    assert fetched.body == "second version"
    assert fetched.tags == ["v2"]
    assert len(store.find_all()) == 1
