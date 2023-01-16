from enum import Enum


class Flavor(Enum):
    VANILLA = 1
    CHOCOLATE = 2
    MINT = 3


# Iterating over members
for flavor in Flavor:
    print(flavor)

# Iterating over members' names
for flavor in Flavor:
    print(flavor.name)

# Iterating over members' value
for flavor in Flavor:
    print(flavor.value)

# Iterating over __members__
for name, member in Flavor.__members__.items():
    print(name, "->", member)
