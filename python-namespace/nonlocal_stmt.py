def f():
    x = 20

    def g():
        nonlocal x
        x = 40

    g()
    print(x)


f()
