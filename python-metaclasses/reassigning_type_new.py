# Spoiler alert: This doesn't work!
def new(cls):
    x = type.__new__(cls)
    x.attr = 100
    return x


try:
    type.__new__ = new
except TypeError as ex:
    print(ex)
