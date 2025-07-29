class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}(name={self.name!r}, age={self.age!r})"


jdoe = Person("John Doe", 42)
print(jdoe)
