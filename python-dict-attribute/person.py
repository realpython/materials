class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "{first_name} {last_name} is {age} years old".format(
            **self.__dict__
        )

    def __repr__(self):
        return "{cls}('{first_name}', '{last_name}', {age})".format(
            cls=type(self).__name__,
            **self.__dict__,
        )

    def as_dict(self):
        return self.__dict__

    def as_tuple(self):
        return tuple(self.__dict__.values())


john = Person("John", "Doe", 30)
print(repr(john))
Person("John", "Doe", 30)
print(john)
print(john.as_dict())
print(john.as_tuple())
