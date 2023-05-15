# Here's another interesting example for debugging your code:


class Stack(list):
    def push(self, item):
        self.append(item)

    def pop(self):
        return super().pop()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self})"


print(Stack([1, 2, 3]))

# Try the following prompt and see how ChatGPT guides you to a solution:

"""
I have a Python class:

class Stack(list):
    def push(self, item):
        self.append(item)
    def pop(self):
        return super().pop()
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self})"

When I call repr() with an instance of this class,
I get <repr-error 'maximum recursion depth exceeded'>

Can you help me fix that?
"""
