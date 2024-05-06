def fizzbuzz(n):
    result = [
        (
            "fizz buzz"
            if i % 15 == 0
            else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else i
        )
        for i in range(1, n + 1)
    ]
    return result
