from datetime import datetime
from uuid import UUID, uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class UserIn(BaseModel):
    name: str


class UserOut(UserIn):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)


users = [
    UserOut(name="Alice"),
    UserOut(name="Bob"),
]


@app.get("/users")
async def get_users():
    return users


@app.post("/users", status_code=201)
async def create_user(user_in: UserIn):
    user_out = UserOut(name=user_in.name)
    users.append(user_out)
    return user_out
