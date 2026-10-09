"""SQLite-backed storage for notes.

Each note is persisted twice:

* as a Markdown file (with YAML frontmatter) on disk, which is the
  canonical, human-editable representation, and
* as a row in a SQLite database, which acts as a fast, queryable index
  used for search/listing operations.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

from . import markdown_io
from .models import Note

_TAG_SEPARATOR = ","

_SCHEMA = """
CREATE TABLE IF NOT EXISTS notes (
    title TEXT PRIMARY KEY,
    body TEXT NOT NULL,
    tags TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL,
    filepath TEXT NOT NULL
);
"""


class NoteStore:
    """Add, search, and retrieve Markdown notes backed by SQLite."""

    def __init__(self, notes_dir: Path | str, db_path: Path | str):
        self.notes_dir = Path(notes_dir)
        self.db_path = Path(db_path)
        self.notes_dir.mkdir(parents=True, exist_ok=True)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        self._conn = sqlite3.connect(self.db_path)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute(_SCHEMA)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> "NoteStore":
        return self

    def __exit__(self, *exc_info) -> None:
        self.close()

    def add_note(self, note: Note) -> Note:
        """Write ``note`` to disk and index it in the database.

        Returns the note as-is (useful when chaining).
        """
        filepath = markdown_io.write_note_file(note, self.notes_dir)
        self._conn.execute(
            """
            INSERT INTO notes (title, body, tags, created_at, filepath)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(title) DO UPDATE SET
                body = excluded.body,
                tags = excluded.tags,
                created_at = excluded.created_at,
                filepath = excluded.filepath
            """,
            (
                note.title,
                note.body,
                _TAG_SEPARATOR.join(note.tags),
                note.created_at.isoformat(),
                str(filepath),
            ),
        )
        self._conn.commit()
        return note

    def reindex(self) -> int:
        """Rebuild the SQLite index from the Markdown files on disk.

        Every ``*.md`` file in ``self.notes_dir`` is read and upserted into
        the database, so files that were added or edited outside of
        :meth:`add_note` (or whose index row was lost) become searchable
        again. Returns the number of notes indexed.
        """
        count = 0
        for path in sorted(self.notes_dir.glob("*.md")):
            created_at = datetime.fromtimestamp(
                path.stat().st_mtime
            ).astimezone()
            note = markdown_io.read_note_file(path, created_at=created_at)
            self.add_note(note)
            count += 1
        return count

    def search_notes(self, query: str) -> list[Note]:
        """
        Return notes whose title or body contains `query` (case-insensitive).
        """
        pattern = f"%{query}%"
        rows = self._conn.execute(
            """
            SELECT * FROM notes
            WHERE title LIKE ? COLLATE NOCASE
               OR body LIKE ? COLLATE NOCASE
            ORDER BY created_at DESC
            """,
            (pattern, pattern),
        ).fetchall()
        return [self._row_to_note(row) for row in rows]

    def find_notes_by_tag(self, tag: str) -> list[Note]:
        """Return all notes tagged with ``tag`` (case-insensitive, exact tag match)."""
        rows = self._conn.execute(
            "SELECT * FROM notes ORDER BY created_at DESC"
        ).fetchall()
        return [
            note
            for row in rows
            if tag.lower() in {t.lower() for t in _split_tags(row["tags"])}
            for note in [self._row_to_note(row)]
        ]

    def find_note_by_title(self, title: str) -> Note | None:
        """Retrieve a single note by its exact title, or ``None`` if not found."""
        row = self._conn.execute(
            "SELECT * FROM notes WHERE title = ?", (title,)
        ).fetchone()
        return self._row_to_note(row) if row else None

    def find_all(self) -> list[Note]:
        """Return every note in the store, most recently created first."""
        rows = self._conn.execute(
            "SELECT * FROM notes ORDER BY created_at DESC"
        ).fetchall()
        return [self._row_to_note(row) for row in rows]

    @staticmethod
    def _row_to_note(row: sqlite3.Row) -> Note:
        return Note(
            title=row["title"],
            body=row["body"],
            tags=_split_tags(row["tags"]),
            created_at=datetime.fromisoformat(row["created_at"]),
        )


def _split_tags(raw: str) -> list[str]:
    return [tag for tag in raw.split(_TAG_SEPARATOR) if tag]
