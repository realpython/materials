"""Command-line interface for the note manager."""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from .markdown_io import note_to_markdown
from .models import Note
from .store import NoteStore

DEFAULT_DB_PATH = Path.home() / ".notes-manager-copilot-test" / "notes.db"


def _notes_dir(db_path: Path) -> Path:
    return db_path.parent / "notes"


def _slugify(title: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", title).strip("_")
    return slug or "untitled"


def _write_note_file(notes_dir: Path, note: Note) -> None:
    notes_dir.mkdir(parents=True, exist_ok=True)
    (notes_dir / f"{_slugify(note.title)}.md").write_text(
        note_to_markdown(note)
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="notes", description="Manage Markdown notes"
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=DEFAULT_DB_PATH,
        help="Path to the SQLite database file",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a note")
    add_parser.add_argument("title")
    add_parser.add_argument("body")
    add_parser.add_argument("--tags", nargs="*", default=[])

    search_parser = subparsers.add_parser(
        "search", help="Search notes by title or body"
    )
    search_parser.add_argument("query")

    list_tag_parser = subparsers.add_parser(
        "list-tag", help="List notes with a given tag"
    )
    list_tag_parser.add_argument("tag")

    get_parser = subparsers.add_parser("get", help="Get a note by title")
    get_parser.add_argument("title")

    return parser


def _print_note(note: Note) -> None:
    print(note_to_markdown(note))
    print()


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    args.db.parent.mkdir(parents=True, exist_ok=True)
    store = NoteStore(args.db)
    try:
        if args.command == "add":
            note = Note(
                title=args.title,
                body=args.body,
                tags=list(args.tags),
                created_at=datetime.now(timezone.utc),
            )
            store.add_note(note)
            _write_note_file(_notes_dir(args.db), note)
            print(f"Added note {note.title!r}")
        elif args.command == "search":
            notes = store.search_notes(args.query)
            if not notes:
                print("No notes found")
            for note in notes:
                _print_note(note)
        elif args.command == "list-tag":
            notes = store.list_by_tag(args.tag)
            if not notes:
                print("No notes found")
            for note in notes:
                _print_note(note)
        elif args.command == "get":
            note = store.get_by_title(args.title)
            if note is None:
                print(f"No note titled {args.title!r}", file=sys.stderr)
                return 1
            _print_note(note)
    finally:
        store.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
