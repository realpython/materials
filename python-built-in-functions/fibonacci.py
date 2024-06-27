class Fibonacci:
    def __init__(self):
        self._cache = [0, 1]

    def __call__(self, index):
        if index < len(self._cache):
            fib_number = self._cache[index]
            print(f"{fib_number} id = {id(fib_number)}")
        else:
            fib_number = self(index - 1) + self(index - 2)
            self._cache.append(fib_number)
        return fib_number
