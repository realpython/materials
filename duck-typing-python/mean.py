from collections.abc import Collection


def mean(sample: Collection) -> float:
    return sum(sample) / len(sample)
