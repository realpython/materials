print("Enter one whole number per input.")
print("Type 0 to stop and display their sum:")

total = 0

while (user_int := int(input("+ "))) != 0:
    if user_int < 0:
        continue
    total += user_int

print(f"{total=}")
