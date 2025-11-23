def debug(func):
    def _debug(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}(args: {args}, kwargs: {kwargs}) -> {result}")
        return result

    return _debug


@debug
def add(a, b):
    return a + b


print(add(5, 6))
