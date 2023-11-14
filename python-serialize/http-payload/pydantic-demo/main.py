from datetime import datetime
from uuid import UUID

import httpx
from pydantic import BaseModel, Field, field_validator


class Metadata(BaseModel):
    uuid: UUID = Field(alias="id")
    created_at: datetime


class User(Metadata):
    name: str

    @field_validator("name")
    def check_user_name(cls, name):
        if name[0].isupper():
            return name
        raise ValueError("name must start with an uppercase letter")


if __name__ == "__main__":
    response = httpx.get("http://localhost:8000/users")
    for item in response.json():
        user = User(**item)
        print(repr(user))
