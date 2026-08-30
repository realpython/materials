"""Command-line interface for the Markdown note manager."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from .models import Note
from .store import NoteStore

DEFAULT_NOTES_DIR = Path("notes")
DEFAULT_DB_PATH = Path("notes.db")


def _parse_tags(raw: str | None) -> list[str]:
    if not raw:
        return []
    return [tag.strip() for tag in raw.split(",") if tag.strip()]


def _read_body(args: argparse.Namespace) -> str:
    if args.body_file:
        return Path(args.body_file).read_text(encoding="utf-8")
    if args.body is not None:
        return args.body
    return sys.stdin.read()


def _print_note(note: Note) -> None:
    tags = ", ".join(note.tags) if note.tags else "-"
    print(f"# {note.title}")
    print(f"tags: {tags}")
    print(f"created_at: {note.created_at.isoformat()}")
    print()
    print(note.body)


def _print_note_summary(note: Note) -> None:
    tags = ", ".join(note.tags) if note.tags else "-"
    print(f"{note.title}\t[{tags}]\t{note.created_at.isoformat()}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="notes",
        description="A command-line Markdown note manager.",
    )
    parser.add_argument(
        "--notes-dir",
        default=DEFAULT_NOTES_DIR,
        type=Path,
        help=f"Directory to store Markdown note files in (default: {DEFAULT_NOTES_DIR})",
    )
    parser.add_argument(
        "--db",
        default=DEFAULT_DB_PATH,
        type=Path,
        help=f"Path to the SQLite index database (default: {DEFAULT_DB_PATH})",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("title", help="Title of the note")
    add_parser.add_argument(
        "--tags", default="", help="Comma-separated list of tags"
    )
    body_group = add_parser.add_mutually_exclusive_group()
    body_group.add_argument("--body", help="Body text of the note")
    body_group.add_argument(
        "--body-file", help="Path to a file containing the note body"
    )

    search_parser = subparsers.add_parser(
        "search", help="Search notes by title or body content"
    )
    search_parser.add_argument("query", help="Text to search for")

    list_tag_parser = subparsers.add_parser(
        "list-tag", help="List notes that have a given tag"
    )
    list_tag_parser.add_argument("tag", help="Tag to filter by")

    get_parser = subparsers.add_parser(
        "get", help="Retrieve a note by its exact title"
    )
    get_parser.add_argument("title", help="Title of the note")

    subparsers.add_parser("list", help="List all notes")

    subparsers.add_parser(
        "reindex",
        help="Rebuild the SQLite search index from the Markdown files on disk",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    with NoteStore(args.notes_dir, args.db) as store:
        if args.command == "add":
            note = Note(
                title=args.title,
                body=_read_body(args),
                tags=_parse_tags(args.tags),
            )
            store.add_note(note)
            print(f"Added note '{note.title}'")
            return 0

        if args.command == "search":
            results = store.find_notes_by_title_and_body(args.query)
            if not results:
                print("No notes found.")
                return 0
            for note in results:
                _print_note_summary(note)
            return 0

        if args.command == "list-tag":
            results = store.find_notes_by_tag(args.tag)
            if not results:
                print(f"No notes found with tag '{args.tag}'.")
                return 0
            for note in results:
                _print_note_summary(note)
            return 0

        if args.command == "get":
            note = store.find_note_by_title(args.title)
            if note is None:
                print(
                    f"No note found with title '{args.title}'.",
                    file=sys.stderr,
                )
                return 1
            _print_note(note)
            return 0

        if args.command == "list":
            results = store.find_all()
            if not results:
                print("No notes found.")
                return 0
            for note in results:
                _print_note_summary(note)
            return 0

        if args.command == "reindex":
            count = store.reindex()
            print(f"Reindexed {count} note(s) from '{args.notes_dir}'.")
            return 0

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
