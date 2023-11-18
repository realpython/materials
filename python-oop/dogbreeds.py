# Heirarchical Inheritance in Python -->
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass

# Try it yourself first ;)

# Creating instances of the classes
dog = Dog("Buddy", 5)
jack = JackRussellTerrier("Jack", 3)
dachshund = Dachshund("Daisy", 4)
bulldog = Bulldog("Rocky", 6)

# Printing information about the instances
print(dog.species)              # Output: Canis familiaris
print(dog)                      # Output: Buddy is 5 years old
print(dog.speak("Woof"))        # Output: Buddy barks: Woof


print(jack.species)             # Output: Canis familiaris
print(jack)                     # Output: Jack is 3 years old
print(jack.speak())             # Output: Jack barks: Arf

print(dachshund.species)        # Output: Canis familiaris
print(dachshund)                # Output: Daisy is 4 years old
print(dachshund.speak("Ruff"))  # Output: Daisy barks: Ruf

print(bulldog.species)          # Output: Canis familiaris
print(bulldog)                  # Output: Rocky is 6 years old
print(bulldog.speak("Grr"))     # Output: Rocky barks: Grr
