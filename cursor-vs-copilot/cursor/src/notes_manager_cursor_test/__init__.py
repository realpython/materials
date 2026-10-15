"""A command-line Markdown note manager."""

from .models import Note
from .store import NoteStore

__all__ = ["Note", "NoteStore"]
