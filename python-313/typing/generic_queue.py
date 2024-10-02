from collections import deque


class Queue[T]:
    def __init__(self) -> None:
        self.elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        return self.elements.popleft()


# %% Python 3.13
#
# class Queue[T=str]:
#     def __init__(self) -> None:
#         self.elements: deque[T] = deque()
#
#     def push(self, element: T) -> None:
#         self.elements.append(element)
#
#     def pop(self) -> T:
#         return self.elements.popleft()

# %% Use the queue
#
string_queue = Queue()
integer_queue = Queue[int]()

string_queue.push("three")
string_queue.push("thirteen")
print(string_queue.elements)

integer_queue.push(3)
integer_queue.push(13)
print(integer_queue.elements)
