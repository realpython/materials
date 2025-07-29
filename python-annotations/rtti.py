from typeguard import typechecked


@typechecked
def add(a: int, b: int) -> int:
    return a + b
