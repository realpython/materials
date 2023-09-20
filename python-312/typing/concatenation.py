def concatenate[T: (str, bytes)](first: T, second: T) -> T:
    return first + second
