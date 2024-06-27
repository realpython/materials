from typing import Optional, Protocol


class LinkedListNode(Protocol):
    value: int
    next_node: Optional["LinkedListNode"]

    def __str__(self) -> str:
        return f"{self.value} -> {self.next_node}"


class Node:
    def __init__(
        self,
        value: int,
        next_node: Optional["LinkedListNode"] = None,
    ):
        self.value = value
        self.next_node = next_node

    def __str__(self) -> str:
        return f"{self.value} -> {self.next_node}"


def print_linked_list(start_node: LinkedListNode):
    print(start_node)


node3 = Node(3)
node2 = Node(2, node3)
node1 = Node(1, node2)

print_linked_list(node1)
