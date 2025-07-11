isinstance(True, int)

isinstance(True, bool)

isinstance(False, int)

isinstance(False, bool)

test_data = [10, True, False]

for element in test_data:
    print("int") if isinstance(element, int) else print("bool")

for element in test_data:
    print("bool") if isinstance(element, bool) else print("int")

for element in test_data:
    print("bool") if type(element) is bool else print("int")  # noqa
