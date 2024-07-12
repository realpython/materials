class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


jane = Person("Jane", 25)
print(getattr(jane, "name"))
print(getattr(jane, "age"))
