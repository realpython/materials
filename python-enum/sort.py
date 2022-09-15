from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


# Sort by name
sorted(Season, key=lambda season: season.name)

# Sort by value
sorted(Season, key=lambda season: season.value)
