from abc import ABC


class Bird(ABC):
    def swim(self):
        raise NotImplementedError("must be implemented in subclasses")

    def fly(self):
        raise NotImplementedError("must be implemented in subclasses")


class Duck(Bird):
    def swim(self):
        print("The duck is swimming")

    def fly(self):
        print("The duck is flying")


class Penguin(Bird):
    def swim(self):
        print("The penguin is swimming")
