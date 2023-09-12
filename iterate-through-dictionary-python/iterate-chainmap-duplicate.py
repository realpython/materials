from collections import ChainMap

for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
pets = ChainMap(for_adoption, vet_treatment)

for pet, count in pets.items():
    print(pet, "->", count)
