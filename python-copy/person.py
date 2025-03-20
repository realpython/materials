import copy
from datetime import date


def in_place():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __replace__(self, **changes):
            if unknown := changes.keys() - self.__dict__.keys():
                raise AttributeError(", ".join(unknown))
            self.__dict__.update(**changes)

    person = Person("John Doe", 42)
    copy.replace(person, age=24, name="Alice Smith")
    print(vars(person))
    # This raises an error:
    # print(copy.replace(person, name="Bob Brown", email="bob.brown@example.com"))


def shallow():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __replace__(self, **changes):
            return type(self)(**self.__dict__ | changes)

    person = Person("John Doe", 42)
    person_copy = copy.replace(person, age=24, name="Alice Smith")
    print(vars(person))
    print(vars(person_copy))
    # This raises an error:
    # print(copy.replace(person, email="bob.brown@example.com"))


def slots():
    class Person:
        __slots__ = ("name", "age")

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __replace__(self, **changes):
            instance = type(self)(self.name, self.age)
            for name, value in changes.items():
                if hasattr(self, name):
                    setattr(instance, name, value)
            return instance

    person = Person("John Doe", 42)
    person_copy = copy.replace(person, age=24, name="Alice Smith")

    vars_slots = lambda obj: {
        name: getattr(obj, name) for name in obj.__slots__
    }

    print(vars_slots(person))
    print(vars_slots(person_copy))


def derived():
    class Person:
        def __init__(self, name, date_of_birth):
            self.name = name
            self.date_of_birth = date_of_birth

        @property
        def age(self):
            return (date.today() - self.date_of_birth).days // 365

        def __replace__(self, **changes):
            age = changes.pop("age", None)
            dob = changes.pop("date_of_birth", None)

            instance = copy.copy(self)
            for name, value in changes.items():
                if hasattr(self, name):
                    setattr(instance, name, value)

            if age and dob:
                raise AttributeError(
                    "can't set both 'age' and 'date_of_birth'"
                )
            elif age:
                dob = copy.replace(date.today(), year=date.today().year - age)
                instance.date_of_birth = dob
            elif dob:
                instance.date_of_birth = dob

            return instance

    person = Person("John Doe", date(1983, 3, 14))
    print(vars(copy.replace(person, age=24)))
    print(vars(copy.replace(person, date_of_birth=date(1999, 6, 15))))
    # This raises an error:
    # print(vars(copy.replace(person, date_of_birth=date(1999, 6, 15), age=12)))


if __name__ == "__main__":
    in_place()
    shallow()
    slots()
    derived()
