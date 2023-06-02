from typing import Any

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item:Any) -> Queue:
        self.items.append(item)
        return self