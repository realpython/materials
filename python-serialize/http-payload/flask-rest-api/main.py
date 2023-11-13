"""
GET Example:
$ curl http://127.0.0.1:5000/users

POST Example:
$ curl -X POST http://127.0.0.1:5000/users \
       -H 'Content-Type: application/json' \
       --data '{"name": "Frank"}'
{
  "created_at": "Sun, 05 Nov 2023 17:34:19 GMT",
  "id": "6f3530f4-2251-49ad-899b-df4c4f47009d",
  "name": "Frank"
}
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from flask import Flask, jsonify, request

app = Flask(__name__)


@dataclass
class User:
    id: UUID
    name: str
    created_at: datetime

    @classmethod
    def create(cls, name):
        return cls(uuid4(), name, datetime.now())


users = [
    User.create("Alice"),
    User.create("Bob"),
]


@app.route("/users", methods=["GET", "POST"])
def view_users():
    if request.method == "GET":
        return users
    elif request.method == "POST":
        if request.is_json:
            payload = request.get_json()
            user = User.create(payload["name"])
            users.append(user)
            return jsonify(user), 201


if __name__ == "__main__":
    app.run(debug=True)
