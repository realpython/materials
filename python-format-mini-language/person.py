class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"


jane = Person("Jane Doe", 25)
print("Hi! {!s}".format(jane))
print("An instance: {!r}".format(jane))
