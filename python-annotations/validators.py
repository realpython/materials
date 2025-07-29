from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import User


def validate_email(user: User):
    if user.email is None:
        raise ValueError("email is required")
