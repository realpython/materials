from collections.abc import Collection


def mean(grades: Collection) -> float:
    return sum(grades) / len(grades)
