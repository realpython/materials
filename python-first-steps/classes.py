class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof! Woof!"


fido = Dog("Fido", 3)
print(fido.name, fido.age)
print(fido.bark())
