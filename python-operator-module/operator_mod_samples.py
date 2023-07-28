import operator

print(operator.truediv(5, 2))  # 5 / 2

print(operator.ge(5, 2))  # 5 >= 2

print(operator.is_("X", "Y"))  # "X" is "Y"

print(operator.not_(5 < 3))  # Not True

print(bin(operator.and_(0b10, 0b11)))  # 0b10 & 0b11
