"""Sample failing tests.

The output must be an integer
>>> 5 + 7
12.0

The output must not contain quotes
>>> print("Hello, World!")
'Hello, World!'

The output must not use double quotes
>>> "Hello," + " World!"
"Hello, World!"

The output must not contain leading or trailing spaces
>>> print("Hello, World!")
  Hello, World!

The traceback doesn't include the correct exception message
>>> raise ValueError("incorrect value")
Traceback (most recent call last):
ValueError: invalid value
"""
