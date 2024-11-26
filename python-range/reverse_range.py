def reverse_range(rng):
    """Explicitly calculate necessary parameters to reverse a general range.

    In practice, you should use reversed() or [::-1] instead.
    """
    adj = 1 if rng.step > 0 else -1
    return range(
        (rng.stop - adj) - (rng.stop - rng.start - adj) % rng.step,
        rng.start - adj,
        -rng.step,
    )


if __name__ == "__main__":
    numbers = range(1, 20, 4)

    print("\nOriginal:")
    print(numbers)
    print(list(numbers))

    print("\nReversed:")
    print(reverse_range(numbers))
    print(list(reverse_range(numbers)))

    print("\nTwice reversed, has the same elements as the original:")
    print(reverse_range(reverse_range(numbers)))
    print(list(reverse_range(reverse_range(numbers))))
