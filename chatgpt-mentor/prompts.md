# Prompts

This file includes the prompts mentioned and used in the associated Real Python tutorial called [ChatGPT: Your Personal Python Coding Mentor](https://realpython.com/chatgpt-coding-mentor-python/).

## Beware of Incorrect and Irrelevant Information

1. Please show me a table with a cheat sheet of Python's syntax.
2. Could you show me the Markdown source of this table so I can copy it?

## Improve Your Results With Prompt Engineering

```
You are an expert Python developer with years of experience writing Python code and teaching Python to other programmers. You have vast experience mentoring people who are learning Python. I want you to be my mentor while I learn Python myself. If you understood, respond with the word "Ok".
```

```
I'd want to have a concise cheat sheet reference of Python's syntax that I can print out on a single page of paper.

Please, generate a Markdown formatted table with Python's most important syntax. The table should list variables, conditionals, loops, functions, classes, imports, exception handling, Boolean operators, math operators, comparison operators, and comprehensions.

It should include the syntax elements, a short explanation of it, and a concise example code snippet that explains it.

For example, here's how the list could begin:

    ```markdown
    | Syntax | Example | Description |
    | --- | --- | --- |
    | Comments | `# Comment` | Notes or explanations in the code and are not executed by the interpreter |
    ```

Please continue this list and make sure to show the most important syntax elements. You can mix HTML into the Markdown to improve the presentation.
```

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

1. What's the difference between a list and a tuple in Python?
2. What's the difference between mutable vs immutable types?
3. Can you show me a real-world example of both a tuple and a list?
4. What are good use cases for a tuple?
5. Please provide some links that explain the topic.

- Please show me the link to the Python documentation that explains `__init__.py`