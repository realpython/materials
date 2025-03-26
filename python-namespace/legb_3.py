x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()


outer()
