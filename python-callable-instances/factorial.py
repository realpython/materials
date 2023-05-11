class Factorial:
    def __init__(self):
        self.cache = {0: 1, 1: 1}

    def __call__(self, number):
        if number not in self.cache:
            self.cache[number] = number * self(number - 1)
        return self.cache[number]
