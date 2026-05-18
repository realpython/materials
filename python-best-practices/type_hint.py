# Avoid this:
# import json
# from typing import Any


# def load_user(raw: str) -> dict[str, Any]:
#     return json.loads(raw)


# def format_user(user: dict[str, Any]) -> str:
#     return f"{user['name']} <{user['email']}>"


# Favor this:
import json
from typing import TypedDict


class UserPayload(TypedDict):
    name: str
    email: str


def load_user(raw: str) -> UserPayload:
    data = json.loads(raw)
    return {
        "name": data["name"],
        "email": data["email"],
    }


def format_user(user: UserPayload) -> str:
    return f"{user['name']} <{user['email']}>"
