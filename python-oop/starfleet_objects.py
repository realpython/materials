# Starfleet employees as objects


class Employee:
    def __init__(self, name, age, position, year_started):
        self.name = name
        self.age = age
        self.position = position
        self.year_started = year_started


kirk = Employee("James Kirk", 34, "Captain", 2265)
spock = Employee("Spock", 35, "Science Officer", 2254)
mccoy = Employee("Leonard McCoy", 137, "Chief Medical Officer", 2266)
