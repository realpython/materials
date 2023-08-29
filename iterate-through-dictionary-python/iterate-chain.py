from itertools import chain

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = chain(for_adoption.items(), vet_treatment.items())

for pet, count in pets:
    print(pet, "->", count)
