import time
from dataclasses import dataclass


@dataclass
class User:
    name: str
    password: str

    def __getstate__(self):
        state = self.__dict__.copy()
        state["timestamp"] = int(time.time())
        del state["password"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        with open("/dev/random", mode="rb") as file:
            self.password = file.read(8).decode("ascii", errors="ignore")
