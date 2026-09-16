class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100


class X(metaclass=Meta):
    pass


print(X.attr)


class Y(metaclass=Meta):
    pass


print(Y.attr)


class Z(metaclass=Meta):
    pass


print(Z.attr)
