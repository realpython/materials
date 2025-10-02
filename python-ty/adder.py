# fmt:off

import warnings

type Number = int | float


def new_adder(x: Number, y: Number) -> Number:
    return x + y


@warnings.deprecated("Use the new_adder() instead")
def legacy_adder(x, y):
    return x + y


if __name__ == "__main__":
    legacy_adder(  # ty: ignore
        42,
        555
    )

    legacy_adder(
        42,
        555
    )  # ty: ignore

    new_adder(a=42, b=555)  # ty: ignore[unknown-argument, missing-argument]
