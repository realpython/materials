x = "global"


def outer():
    x = "enclosing"  # noga

    def inner():
        x = "local"
        print(x)

    inner()


outer()
