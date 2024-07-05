class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old."


john = Person("John Doe", 35)

print(repr(john))

print(str(john))
