from dataclasses import dataclass

from validators import validate_email


@dataclass
class User:
    email: str
    password: str

    def __post_init__(self):
        validate_email(self)
