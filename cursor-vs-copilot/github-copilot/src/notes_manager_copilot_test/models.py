"""Data model for notes."""

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Note:
    """A single note."""

    title: str
    body: str
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    is_archived: bool = False
