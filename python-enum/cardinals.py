from enum import Enum, auto

# class CardinalDirection(Enum):
#     NORTH = "N"
#     SOUTH = "S"
#     EAST = "E"
#     WEST = "W"


class CardinalDirection(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name[0]

    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


for point in CardinalDirection:
    print(point.name, "->", point.value)
