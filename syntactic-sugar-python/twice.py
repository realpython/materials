class Twice:
    def __init__(self, items):
        self.items = list(items)

    def __iter__(self):
        yield from self.items
        print("Halfway there!")
        yield from self.items


for number in Twice([1, 2, 3]):
    print(f"-> {number}")
