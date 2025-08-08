class A:
    def __init__(self):
        self.__attr = 0

    def __method(self):
        print("A.__attr = ", self.__attr)


class B(A):
    def __init__(self):
        super().__init__()
        self.__attr = 1  # Doesn't override A.__attr

    def __method(self):  # Doesn't override A.__method()
        print("B.__attr = ", self.__attr)


if __name__ == "__main__":
    a = A()
    b = B()

    # Call the mangled methods
    print(f"{a._A__method()=}")
    print(f"{b._B__method()=}")

    # Check attributes
    print(f"{a.__dict__=}")
    print(f"{b.__dict__=}")

    # Access the attributes on b
    print(f"{b._A__attr=}")
    print(f"{b._B__attr=}")
