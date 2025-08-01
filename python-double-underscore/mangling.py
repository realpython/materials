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
