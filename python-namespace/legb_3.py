x = "global"


def outer():
    x = "enclosing"  # noqa

    def inner():
        x = "local"
        print(x)

    inner()


outer()
