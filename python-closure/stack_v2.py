def Stack():
    _items = []

    def push(item):
        _items.append(item)

    def pop():
        return _items.pop()

    def closure():
        pass

    closure.push = push
    closure.pop = pop
    return closure


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.pop()

stack._items
