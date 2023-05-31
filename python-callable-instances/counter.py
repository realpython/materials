class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def __call__(self):
        self.increment()
