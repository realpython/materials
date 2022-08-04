string_code = """
def sum_of_even_squares(numbers):
    return sum(number**2 for number in numbers if number % 2 == 0)

print(sum_of_even_squares(numbers))
"""

compiled_code = compile(string_code, "<string>", "exec")
exec(compiled_code)

numbers = [2, 3, 7, 4, 8]
exec(compiled_code)

numbers = [5, 3, 9, 6, 1]
exec(compiled_code)
