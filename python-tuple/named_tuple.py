from collections import namedtuple

Person = namedtuple("Person", "name age position")

person = Person("John", 35, "Python Developer")
person.name
person.age
person.position
person[0]
