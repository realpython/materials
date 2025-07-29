print(f"{isinstance(True, int) = }")
print(f"{isinstance(True, bool) = }")
print(f"{isinstance(False, int) = }")
print(f"{isinstance(False, bool) = }")

test_data = [10, True, False]

print()
for element in test_data:
    print("int") if isinstance(element, int) else print("bool")

print()
for element in test_data:
    print("bool") if isinstance(element, bool) else print("int")

print()
for element in test_data:
    print("bool") if type(element) is bool else print("int")  # noqa
