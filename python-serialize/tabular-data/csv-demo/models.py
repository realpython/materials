import random
from datetime import datetime
from enum import StrEnum
from typing import NamedTuple

from faker import Faker


class Language(StrEnum):
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    IT = "it"


class User(NamedTuple):
    id: int
    name: str
    email: str
    language: Language
    registered_at: datetime

    @classmethod
    def fake(cls):
        language = random.choice(list(Language))
        generator = Faker(language)
        return cls(
            generator.pyint(),
            generator.name(),
            generator.email(),
            language,
            generator.date_time_this_year(),
        )

    @classmethod
    def from_dict(cls, row_dict):
        transforms = {
            "id": int,
            "name": str.title,
            "language": Language,
            "registered_at": datetime.fromisoformat,
        }
        return cls(
            **{
                key: transforms.get(key, lambda x: x)(value)
                for key, value in row_dict.items()
            }
        )
