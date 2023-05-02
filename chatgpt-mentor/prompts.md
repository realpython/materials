# Prompts

This file includes the prompts mentioned and used in the associated Real Python tutorial called [ChatGPT: Your Personal Python Coding Mentor](https://realpython.com/chatgpt-coding-mentor-python/).

## Beware of Incorrect and Irrelevant Information

1. Please show me a table with a cheatsheet of Python's syntax
2. Could you show me the Markdown source of this table so I can copy it?

## Debug Your Code With ChatGPT’s Help

```
>>> current_age = input("Enter your current age: ")
Enter your current age: 36
>>> print("Next year you'll be:", current_age + 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

```
>>> 3 plus 4
  File "<stdin>", line 1
    3 plus 4
      ^^^^
SyntaxError: invalid syntax
```

```
>>> from collections import chainmap
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'chainmap' from 'collections'
⮑ (/Users/martin/.pyenv/versions/3.11.0/lib/python3.11/collections/__init__.py)
```

```
def fizzbuzz(number):
    if number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 15 == 0:
        return "fizz buzz"
    else:
        return number
```

## Pair-Program With ChatGPT and Write Better Code

```
import random

num = random.randint(1, 100)
i = None

while i != num:
    i = int(input("Guess the number: "))
    if i < num:
        print("Too low")
    elif i > num:
        print("Too high")
    else:
        print("Correct!)

How can I improve this code?
```

```
import random

num = random.randint(1, 100)
i = None

while i != num:
    i = int(input("Guess the number: "))
    if i < num:
        print("Too low")
    elif i > num:
        print("Too high")
    else:
        print("Correct!)

How can I improve variable naming in this code example?
```

- Could you also improve the messages a user will read when interacting with this program?
- Can you refactor the code into a function?
- Please refactor the code so that `1` and `100` are default arguments. Also use an f-string to fix the input text message accordingly.
- How can I save the randomly generated number?
- Could you also add type hinting and a docstring to the function?

## Prompt ChatGPT for Alternative Implementations

```
def fizzbuzz(number):
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number

What are alternative implementations of this problem?
```

## Get Answers to Your Programming Question

1. What's the difference between an abstract class and an interface?
2. Can you show me an example of both an abstract class and an interface?
3. What are good use cases for an interface?
4. How does this apply to Python?
5. Please provide some links that explain the topic

- Please show me the link to the Python documentation that explains `__init__.py`