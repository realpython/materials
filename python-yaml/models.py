# models.py

import codecs
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str


class User:
    __slots__ = ["name"]

    def __init__(self, name):
        self.name = name

    def __setstate__(self, state):
        self.name = codecs.decode(state["name"], "rot13")
