from datetime import datetime

import pytest

from notes_manager_copilot_test.models import Note
from notes_manager_copilot_test.store import NoteStore


@pytest.fixture
def store(tmp_path):
    db_path = tmp_path / "notes.db"
    note_store = NoteStore(db_path)
    yield note_store
    note_store.close()


def test_add_and_get_by_title(store):
    note = Note(
        title="Groceries",
        body="Milk, eggs",
        tags=["home"],
        created_at=datetime(2024, 1, 1),
    )
    store.add_note(note)

    fetched = store.get_by_title("Groceries")
    assert fetched is not None
    assert fetched.title == "Groceries"
    assert fetched.body == "Milk, eggs"
    assert fetched.tags == ["home"]
    assert fetched.created_at == datetime(2024, 1, 1)


def test_get_by_title_missing_returns_none(store):
    assert store.get_by_title("Nope") is None


def test_search_notes(store):
    store.add_note(
        Note(
            title="Trip plan",
            body="Visit museum",
            tags=["travel"],
            created_at=datetime(2024, 1, 1),
        )
    )
    store.add_note(
        Note(
            title="Recipe",
            body="Bake bread",
            tags=["food"],
            created_at=datetime(2024, 1, 2),
        )
    )

    results = store.search_notes("museum")
    assert len(results) == 1
    assert results[0].title == "Trip plan"

    title_results = store.search_notes("Recipe")
    assert len(title_results) == 1
    assert title_results[0].title == "Recipe"

    assert store.search_notes("nonexistent") == []


def test_list_by_tag(store):
    store.add_note(
        Note(
            title="A", body="a", tags=["work"], created_at=datetime(2024, 1, 1)
        )
    )
    store.add_note(
        Note(
            title="B",
            body="b",
            tags=["personal"],
            created_at=datetime(2024, 1, 2),
        )
    )
    store.add_note(
        Note(
            title="C",
            body="c",
            tags=["work", "urgent"],
            created_at=datetime(2024, 1, 3),
        )
    )

    work_notes = store.list_by_tag("work")
    assert {n.title for n in work_notes} == {"A", "C"}

    assert store.list_by_tag("missing") == []
