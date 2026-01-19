# Avoid this:
# cubes = []
# for number in range(10):
#     cubes.append(number**3)

# Favor this:
cubes = [number**3 for number in range(10)]
cubes
