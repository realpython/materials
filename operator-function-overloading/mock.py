class Mock:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Mock(self.num + other)
