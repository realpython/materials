from typing import Annotated

from fastapi import Header, HTTPException

# In-memory stand-in for a real database.
FAKE_DB = {
    "authors": {
        1: {"id": 1, "name": "Ursula K. Le Guin"},
        2: {"id": 2, "name": "Terry Pratchett"},
    },
    "books": {
        1: {"id": 1, "title": "A Wizard of Earthsea", "author_id": 1},
        2: {"id": 2, "title": "Guards! Guards!", "author_id": 2},
    },
}


def get_db():
    """Provide a database session to path operations."""
    yield FAKE_DB


async def get_token_header(x_token: Annotated[str, Header()]):
    """Allow only requests that send the expected admin token."""
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
