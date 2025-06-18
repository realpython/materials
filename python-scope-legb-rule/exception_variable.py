numbers = [1, 2, 3]

try:
    numbers[4]
except IndexError as error:
    # The variable error is local to this block
    exception = error
    error


print(exception)
