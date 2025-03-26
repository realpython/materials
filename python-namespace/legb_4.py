def outer():
    def inner():
        print(x)

    inner()


outer()
