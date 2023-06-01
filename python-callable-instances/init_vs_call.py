class Demo:
    def __init__(self, attr):
        print(f"Initialize an instance of {self.__class__.__name__}")
        self.attr = attr
        print(f"{self.attr=}")

    def __call__(self, arg):
        print(f"Call an instance of {self.__class__.__name__} with {arg}")
