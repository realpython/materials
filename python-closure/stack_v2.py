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
