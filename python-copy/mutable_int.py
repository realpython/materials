class MutableInt:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    x = MutableInt(40)
    x += 2
    print(x)
