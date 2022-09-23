from enum import Enum


class AtlanticAveSemaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    PEDESTRIAN_RED = 1
    PEDESTRIAN_GREEN = 3


class EighthAveSemaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    PEDESTRIAN_RED = 1
    PEDESTRIAN_GREEN = 3


red = AtlanticAveSemaphore.RED
print(f"{red is AtlanticAveSemaphore.RED = }")
print(f"{red is not AtlanticAveSemaphore.RED = }")

yellow = AtlanticAveSemaphore.YELLOW
print(f"{yellow is red = }")
print(f"{yellow is not red = }")

pedestrian_red = AtlanticAveSemaphore.PEDESTRIAN_RED
print(f"{red is pedestrian_red = }")
