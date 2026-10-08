def decorator(cls):
    class NewClass(cls):
        attr = 100

    return NewClass


@decorator
class X:
    pass


@decorator
class Y:
    pass


@decorator
class Z:
    pass


print(X.attr)
print(Y.attr)
print(Z.attr)
