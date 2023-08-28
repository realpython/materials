for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}

for pet, count in {**for_adoption, **vet_treatment}.items():
    print(pet, "->", count)
