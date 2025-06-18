class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, *_):
        self.level -= 1

    def print(self, text):
        print("    " * self.level + text)
