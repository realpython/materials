name_list = ["Ainslie", "Dieter", "Gabey", "Carena", "Allina", "Aila"]

SEARCHING_FOR = "Carena"

for name in name_list:
    if name == SEARCHING_FOR:
        print(f"Found {name}")
        break
else:
    print("Not found")
