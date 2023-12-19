class BitwiseNumber:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return type(self)(self.value & other.value)

    def __or__(self, other):
        return type(self)(self.value | other.value)

    def __xor__(self, other):
        return type(self)(self.value ^ other.value)

    def __invert__(self):
        return type(self)(~self.value)

    def __lshift__(self, places):
        return type(self)(self.value << places)

    def __rshift__(self, places):
        return type(self)(self.value >> places)

    def __repr__(self):
        return bin(self.value)
