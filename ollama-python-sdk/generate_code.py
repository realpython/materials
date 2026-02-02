from ollama import generate

prompt = """
Write a Python function fizzbuzz(n: int) -> List[str] that:

- Returns a list of strings for the numbers 1..n
- Uses "Fizz" for multiples of 3
- Uses "Buzz" for multiples of 5
- Uses "FizzBuzz" for multiples of both 3 and 5
- Uses the number itself (as a string) otherwise
- Raises ValueError if n < 1

Include type hints compatible with Python 3.8.
"""

response = generate(model="codellama:latest", prompt=prompt)
print(response.response)
