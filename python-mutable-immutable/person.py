class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major


john = Student("John", "Computer Science")
print(type(john))
john.__class__ = Person
print(john.name)
print(john.major)
print(type(john))
