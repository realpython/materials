class Fibonaccish:
    def __init__(self, initial_value=1):
        self._cache = [0, initial_value]

    def __call__(self, index):
        if index < len(self._cache):
            fib_number = self._cache[index]
            print(f"{index} {fib_number} id = {id(fib_number)}")
        else:
            fib_number = self(index - 1) + self(index - 2)
            self._cache.append(fib_number)
        return fib_number
