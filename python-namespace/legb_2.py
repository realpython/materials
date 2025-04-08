x = "global"


def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()


outer()
