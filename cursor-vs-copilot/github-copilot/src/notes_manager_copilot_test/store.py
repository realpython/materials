"""SQLite-backed storage for notes."""

import json
import sqlite3
from datetime import datetime
from os import PathLike

from .models import Note

_SCHEMA = """
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    body TEXT NOT NULL,
    tags TEXT NOT NULL,
    created_at TEXT NOT NULL
)
"""


class NoteStore:
    """Stores and queries notes in a SQLite database."""

    def __init__(self, db_path: str | PathLike[str]) -> None:
        self._conn = sqlite3.connect(db_path)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute(_SCHEMA)
        self._conn.commit()

    def add_note(self, note: Note) -> None:
        """Insert a new note into the store."""
        self._conn.execute(
            "INSERT INTO notes (title, body, tags, created_at) VALUES (?, ?, ?, ?)",
            (
                note.title,
                note.body,
                json.dumps(note.tags),
                note.created_at.isoformat(),
            ),
        )
        self._conn.commit()

    def search_notes(self, query: str) -> list[Note]:
        """Return notes whose title or body contains the given query text."""
        rows = self._conn.execute(
            "SELECT * FROM notes WHERE title LIKE ? OR body LIKE ? ORDER BY created_at",
            (f"%{query}%", f"%{query}%"),
        ).fetchall()
        return [self._row_to_note(row) for row in rows]

    def list_by_tag(self, tag: str) -> list[Note]:
        """Return notes tagged with the given tag."""
        rows = self._conn.execute(
            "SELECT * FROM notes ORDER BY created_at"
        ).fetchall()
        return [
            note
            for row in rows
            if tag in (note := self._row_to_note(row)).tags
        ]

    def get_by_title(self, title: str) -> Note | None:
        """Return the note with the given title, or None if it doesn't exist."""
        row = self._conn.execute(
            "SELECT * FROM notes WHERE title = ?", (title,)
        ).fetchone()
        return self._row_to_note(row) if row is not None else None

    def close(self) -> None:
        """Close the underlying database connection."""
        self._conn.close()

    @staticmethod
    def _row_to_note(row: sqlite3.Row) -> Note:
        return Note(
            title=row["title"],
            body=row["body"],
            tags=json.loads(row["tags"]),
            created_at=datetime.fromisoformat(row["created_at"]),
        )
