def create_plus(x):
    def plus(y):
        return x + y

    return plus


plus_one = create_plus(1)
plus_two = lambda x: x + 2  # noqa
