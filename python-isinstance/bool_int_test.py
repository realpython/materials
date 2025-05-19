isinstance(True, int)

isinstance(True, bool)

isinstance(False, int)

isinstance(False, bool)

test_data = [10, True, False]

for element in test_data:
    "int" if isinstance(element, int) else "bool"

for element in test_data:
    "bool" if isinstance(element, bool) else "int"

# Try and avoid this.
# for element in test_data:
#     "bool" if type(element) is bool else "int"
