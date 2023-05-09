class Factorial:
    def __init__(self):
        self.cache = {0: 1, 1: 1}

    def __call__(self, number):
        if number in self.cache:
            return self.cache[number]
        else:
            self.cache[number] = number * self.__call__(number - 1)
            return self.cache[number]
