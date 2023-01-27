# def fibonacci_generator(stop):
#     previous, next = 0, 1
#     for _ in range(0, stop):
#         fib_number = previous
#         previous, next = next, previous + next
#         yield fib_number


def fibonacci_generator(stop=100):
    previous, next = 0, 1
    index = 0
    while True:
        if index == stop:
            return
        index += 1
        fib_number = previous
        previous, next = next, previous + next
        yield fib_number


print("Fibonacci Generator")
for fib in fibonacci_generator(10):
    print(fib)
