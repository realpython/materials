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


class Sort(Enum):
    ASCENDING = 1
    DESCENDING = 2

    def __call__(self, values):
        return sorted(values, reverse=self is Sort.DESCENDING)


numbers = [5, 2, 7, 6, 3, 9, 8, 4]

Sort.ASCENDING(numbers)

Sort.DESCENDING(numbers)
