class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    # def __iter__(self):
    #     yield from self.items

    def __contains__(self, item):
        return item in self.items

    # def __getitem__(self, index):
    #     return self.items[index]
