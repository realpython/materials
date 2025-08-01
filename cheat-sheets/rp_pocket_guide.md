---
marp: true
theme: rp-cheat-sheet-theme
footer: ' '
title: Real Python Pocket Guide
description: Cheat Sheet
url: realpython.com
---

<div class="flex column-image">

<div class="flex-col-1">

![](images/realpython-secondary-logo.png)

</div>

<div class="flex-col-1">

<div class="intro">

# Pocket Reference


Visit [realpython.com](https://www.realpython.com) to turbocharge your Python learning with in-depth Tutorials, real-world examples, and expert guidance.

</div>

</div>

</div>

<br/>

## 🚀 Getting Started

### Interacting With Python
```python
$ python
>>> print("Hello, Python!")
Hello, Python!
```

### Running a script
```console
$ python my_script.py
```

<div class="resources">

### Related Tutorials

- [Python Basics: Start With the Python Interpreter](https://realpython.com/search?q=python+interpreter+repl)
- [Beginner's Guide: Python Basics Tutorials](https://realpython.com/tutorials/basics/)
- [Run Python Scripts From the Command Line](https://realpython.com/search?q=run+python+script)
- [Command-Line Tutorials at Real Python](https://realpython.com/tutorials/command-line/)

</div>

## 📦 Variables & Data Types

### Basic Types
```pycon
>>> 42            # int — Whole numbers
42
>>> 3.14          # float — Decimal numbers
3.14
>>> "Hello"       # str — Text/strings
'Hello'
>>> True          # bool — Boolean values
True
>>> None          # NoneType — Absence of value
```

### Variable Assignment
```python
name = "Leo"           # String
age = 7                # Integer
height = 5.6           # Float
is_cat = True          # Boolean
flaws = None           # None type
```

### String Formatting
```python
f_string = f"{name} is {age} years"
print(f_string)
# "Leo is 7 years"
```

### Check Type and Conversion
```python
type(age)              # <class 'int'>
isinstance(age, int)   # True

int("42")              # 42
float("3.14")          # 3.14
str(42)                # "42"
```

<div class="resources">

### Related Tutorials

- [Variables in Python: Usage and Best Practices](https://realpython.com/python-variables/)
- [Python Basics Tutorials (Types & Values)](https://realpython.com/tutorials/basics/)
- [Python's Assignment Operator: Write Robust Assignments](https://realpython.com/python-assignment-operator/)
- [The Walrus Operator: Python's Assignment Expressions](https://realpython.com/python-walrus-operator/)
- [Python f-Strings: Effortless String Formatting](https://realpython.com/python-f-strings/)
- [Python String Formatting Best Practices](https://realpython.com/string-formatting-in-python/)
- [Type Checking in Python](https://realpython.com/search?q=type+checking+isinstance)

</div>

## 📝 Strings

### String Basics
```python
# Creating strings
single = 'Hello'
double = "World"
multi = """Multiple
line string"""

# String operations
greeting = "me" + "ow!"
repeat = "Meow!" * 3
length = len("Python")
```

### String Methods
```pycon
>>> "a".upper()                       # str.upper()
'A'
>>> "A".lower()                       # str.lower()
'a'
>>> " a ".strip()                     # str.strip()
'a'
>>> "abc".replace("bc", "ha")         # str.replace()
'aha'
>>> "a b".split()                     # str.split()
['a', 'b']
>>> "-".join(['a', 'b'])              # str.join()
'a-b'
```

<br class="column-break" />
<br class="column-break" />


### String Indexing & Slicing
```python
text = "Python"
text[0]      # 'P' (first)
text[-1]     # 'n' (last)
text[1:4]    # 'yth' (slice)
text[:3]     # 'Pyt' (from start)
text[3:]     # 'hon' (to end)
text[::2]    # 'Pto' (every 2nd)
text[::-1]   # 'nohtyP' (reverse)
```

<div class="resources">

### Related Tutorials

- [Strings and Character Data in Python](https://realpython.com/python-strings/)
- [String Tutorials on Real Python](https://realpython.com/tutorials/strings/)
- [Essential String Methods in Python](https://realpython.com/search?q=python+string+methods)
- [Python Slice Notation Explained](https://realpython.com/search?q=python+slice+notation)

</div>

## 🔢 Numbers & Math

### Arithmetic Operators
```pycon
>>> 10 + 3     # Addition
13
>>> 10 - 3     # Subtraction
7
>>> 10 * 3     # Multiplication
30
>>> 10 / 3     # Division (float)
3.3333333333333335
>>> 10 // 3    # Floor division
3
>>> 10 % 3     # Modulo
1
>>> 2 ** 3     # Exponentiation
8
```

### Useful Functions
```python
abs(-5)              # 5
round(3.7)           # 4
round(3.14159, 2)    # 3.14
min(1, 2, 3)         # 1
max(1, 2, 3)         # 3
sum([1, 2, 3])       # 6
```

### Type conversion
```python
int("42")            # 42
float("3.14")        # 3.14
str(42)              # "42"
```

<div class="resources">

### Related Tutorials

- [Arithmetic Operators in Python](https://realpython.com/search?q=python+operators)
- [Math and Numerical Computing Tutorials](https://realpython.com/search?q=math+module+python)
- [Python's Built-in Functions](https://realpython.com/search?q=built-in+functions)
- [Converting Types in Python](https://realpython.com/search?q=type+conversion+python)

</div>

## 📊 Collections

### Creating Lists
```python
nums = [5]
mixed = [1, "two", 3.0, True]
empty = []
```

### List Methods
```pycon
>>> nums = [5]                        # start list
>>> nums.append("x")                  # add to end
>>> nums
[5, 'x']
>>> nums.insert(0, "y")               # insert at index 0
>>> nums
['y', 5, 'x']
>>> nums.extend(["z", 5])             # extend with iterable
>>> nums
['y', 5, 'x', 'z', 5]
>>> nums.remove("x")                  # remove first "x"
>>> nums
['y', 5, 'z', 5]
>>> last = nums.pop()                 # pop returns last element
>>> nums
['y', 5, 'z']
>>> last                              # popped value
5
```

### List Indexing & Checks
```python
fruits = ["banana", "apple", "orange"]
fruits[0]              # "banana"
fruits[-1]             # "orange"
"apple" in fruits      # True
len(fruits)            # 3
```

### Tuples
```python
# Creating Tuples
>>> point = (3, 4)
>>> single = (1,)          # Note the comma!
>>> empty = ()

# Tuple Unpacking
>>> point = (3, 4)
>>> x, y = point               # basic unpacking
>>> x
3
>>> y
4
>>> first, *rest = (1, 2, 3, 4) # extended unpacking
>>> first
1
>>> rest
[2, 3, 4]
```

---

### Sets
```python
# Creating Sets
>>> a = {1, 2, 3}
>>> b = set([3, 4, 4, 5])

# Set Operations
>>> a = {1, 2, 3}
>>> b = {3, 4, 5}
>>> a | b        # Union
{1, 2, 3, 4, 5}
>>> a & b        # Intersection
{3}
>>> a - b        # Difference
{1, 2}
>>> a ^ b        # Symmetric difference
{1, 2, 4, 5}
```

### Dictionaries
```python
# Creating Dictionaries
>>> pet = {"name": "Leo", "age": 42}
>>> empty = {}

# Dictionary Operations
>>> pet["sound"] = "Purr!"   # Add key and value
>>> pet["age"] = 7           # Update value
>>> age = pet.get("age", 0)  # Get with default
>>> del pet["email"]         # Delete key
>>> pet.pop("age")           # Remove & return

# Dictionary Methods
>>> pet = {"name": "Leo", "age": 7, "sound": "Purr!"}
>>> pet.keys()             # view keys
dict_keys(['name', 'age', 'sound'])
>>> pet.values()           # view values
dict_values(['Leo', 7, 'Purr!'])
>>> pet.items()            # key/value pairs
dict_items([('name', 'Leo'), ('age', 7), ('sound', 'Purr!')])
```

<div class="resources">

### Related Tutorials

- [Lists and Tuples in Python](https://realpython.com/search?q=lists+and+tuples)
- [Common List Methods in Python](https://realpython.com/search?q=list+methods)
- [Python Lists: Beyond the Basics](https://realpython.com/search?q=python+lists)
- [Indexing and Slicing Lists in Python](https://realpython.com/search?q=list+indexing+slicing)
- [Membership Tests With `in` and `not in`](https://realpython.com/search?q=python+membership+operator)
- [Python Tuples: When to Use Them](https://realpython.com/search?q=python+tuples)
- [Unpacking in Python: Beyond the Basics](https://realpython.com/search?q=python+unpacking)
- [Sets in Python](https://realpython.com/python-sets/)
- [Set Operations and Use Cases](https://realpython.com/search?q=set+operations+python)
- [Dictionaries in Python](https://realpython.com/search?q=python+dictionaries)
- [Mastering Dictionaries in Python](https://realpython.com/search?q=dictionary+methods+python)
- [Dictionary Views: `keys()`, `values()`, and `items()`](https://realpython.com/search?q=dictionary+views)
- [Data Structures Tutorials](https://realpython.com/tutorials/data-structures/)

</div>

<br class="column-break" />

## 🔀 Control Flow

### If--Elif--Else
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Comparison & Boolean
```pycon filename="
>>> 3 == 3             # Equal
True
>>> 3 != 4             # Not equal
True
>>> 2 < 5              # Less than
True
>>> 2 <= 2             # Less or equal
True
>>> (3 > 1) and (2 > 1)   # both True
True
>>> (3 > 5) or (2 < 4)    # either True
True
>>> not (3 == 4)       # opposite
True
```

<div class="resources">

### Related Tutorials

- [Conditional Statements in Python](https://realpython.com/search?q=if+elif+else+python)
- [Comparison, Logical, and Identity Operators](https://realpython.com/search?q=python+operators)
- [Truthy and Falsy in Python](https://realpython.com/search?q=truthy+falsy+python)
- [Python Basics Tutorials](https://realpython.com/tutorials/basics/)

</div>

## 🔁 Loops

### Looping
```python
# Loop 0--4
for i in range(5):
    print(i)

# Loop 1-5
for i in range(1, 5+1):
    print(i)

# Loop Over Collection
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

```python
# Enumerate With Index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Zip Multiple Lists
names = ["Lyra", "Adrian"]
ages = [5, 3]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### Break & Continue in while
```python
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    if user_input == "skip":
        continue
    print(user_input)
```

<div class="resources">

### Related Tutorials

- [Python `for` Loops (Definite Iteration)](https://realpython.com/python-for-loop/)
- [The `range()` Function](https://realpython.com/python-range/)
- [Effective Use of `range()`](https://realpython.com/python-range/)
- [Looping Patterns in Python](https://realpython.com/search?q=loop+patterns+python)
- [Iterating in Python](https://realpython.com/search?q=iterate+over+list+python)
- [`enumerate()` in Python: Loop With Counters](https://realpython.com/python-enumerate/)
- [`zip()` in Python: Parallel Iteration](https://realpython.com/python-zip-function/)
- [Python `while` Loops (Indefinite Iteration)](https://realpython.com/python-while-loop/)
- [Control Flow: `break`, `continue`, and `pass`](https://realpython.com/search?q=break+continue+pass+python)

</div>

## 🛠️ List Comprehensions

### List Comprehensions
```python
# Basic
squares = [x**2 for x in range(10)]

# With Condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Other Comprehensions
```python
# Dictionary Comprehension
word_lengths = {word: len(word) for word in ["hello", "world"]}

# Set Comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey"]}
```

<br class="column-break" />
<br class="column-break" />
<br class="column-break" />
<br class="column-break" />


<div class="resources">

### Related Tutorials

- [List Comprehensions in Python](https://realpython.com/search?q=list+comprehensions+python)
- [Python `for` Loops vs Comprehensions](https://realpython.com/python-for-loop/)
- [Filter With Comprehensions](https://realpython.com/search?q=conditional+list+comprehension)
- [Idiomatic Python: Comprehensions](https://realpython.com/search?q=idiomatic+python+comprehensions)
- [Nested Comprehensions](https://realpython.com/search?q=nested+comprehensions)
- [Dictionary Comprehensions in Python](https://realpython.com/search?q=dictionary+comprehension)
- [Set Comprehensions in Python](https://realpython.com/search?q=set+comprehension)
- [Data Structures Tutorials](https://realpython.com/tutorials/data-structures/)

</div>

## 🔧 Functions

| Function              | Example                       |
| --------------------- | ----------------------------- |
| No Parameters         | `def greet(): ...`            |
| One Parameter         | `def greet(name): ...`        |
| Default Parameter     | `def greet(name="Everyone"): ...` |

### Multiple Return Values
```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(10, 3)
```

### Lambda Functions
```python
square = lambda x: x**2
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

<div class="resources">

### Related Tutorials

- [Defining Your Own Python Functions](https://realpython.com/search?q=define+functions+python)
- [Functions Tutorial Index](https://realpython.com/tutorials/functions/)
- [Returning Multiple Values in Python](https://realpython.com/search?q=multiple+return+values+python)
- [Tuple Unpacking and Assignment](https://realpython.com/search?q=tuple+unpacking)
- [How to Use Python Lambda Functions](https://realpython.com/python-lambda/)
- [Functional Tools: `map()` and `filter()`](https://realpython.com/search?q=python+map+filter)

</div>

---

## 📁 File I/O

### File Operations
```python
# Read Entire File
with open("file.txt", mode="r") as file:
    content = file.read()

# Read File Line by Line
with open("file.txt", mode="r") as file:
    for line in file:
        print(line.strip())

# Write a File
with open("output.txt", mode="w") as file:
    file.write("Hello, World!\n")

# Append to a File
with open("log.txt", mode="a") as file:
    file.write("New log entry\n")
```

<div class="resources">

### Related Tutorials

- [Reading and Writing Files in Python](https://realpython.com/search?q=reading+and+writing+files+in+python)
- [The `open()` Function Explained](https://realpython.com/search?q=open+function+python)
- [Read Text Files Line by Line in Python](https://realpython.com/search?q=read+file+line+by+line+python)
- [Write to Files in Python](https://realpython.com/search?q=write+to+file+python)
- [Append to Files With Python](https://realpython.com/search?q=append+to+file+python)
- [File Modes and Context Managers](https://realpython.com/search?q=file+modes+context+manager+python)

</div>

## ⚠️ Error Handling

### Try/Except/Else/Finally
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No errors occurred")
finally:
    print("This always runs")
```

### Common exceptions
```python
# ValueError
# IndexError
# KeyError
# FileNotFoundError
```

<div class="resources">

### Related Tutorials

- [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- [The `try`/`except`/`else`/`finally` Blocks](https://realpython.com/search?q=try+except+else+finally+python)
- [Common Python Exceptions and How to Handle Them](https://realpython.com/search?q=common+python+exceptions)
- [Exception Hierarchy and Best Practices](https://realpython.com/search?q=exception+hierarchy+python)

</div>

## 📦 Working With JSON (and Dates)

### Working With JSON
```python
# JSON String to Dict
import json

data = json.loads('{"name": "Frieda", "age": 8}')

# Dict to JSON String
data_json = json.dumps({"name": "Frieda", "age": 8})

# Write Dict to JSON File
data = {"name": "Frieda", "age": 8}
with open("output.json", mode="w") as f:
    json.dump(data, f, indent=2)

# Load JSON File as Dict
with open("output.json", mode="r") as f:
    data = json.load(f)
```

### Dates and Times
```python
from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)

print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2025-07-31 20:01:16
```

<div class="resources">

### Related Tutorials

- [Working With JSON Data in Python](https://realpython.com/python-json/)
- [Serialize and Deserialize JSON](https://realpython.com/search?q=json+loads+dumps+python)
- [Write JSON to Files in Python](https://realpython.com/search?q=write+json+file+python)
- [Read JSON From Files in Python](https://realpython.com/search?q=read+json+file+python)
- [Python Datetime: Working With Dates and Times](https://realpython.com/python-datetime/)
- [Mastering `strftime` and `strptime`](https://realpython.com/search?q=strftime+strptime+python)

</div>

## 💡 Miscellaneous

### Truthy and Falsy
```python
# Falsy Values
False
None
0
0.0
""
[]
{}
()

# Truthy List Check
if my_list:
    print(my_list)
```

### Pythonic Constructs
```python
# Swap Variables
a, b = b, a

# Flatten List
flat = [item for sublist in nested for item in sublist]

# Remove Duplicates, Preserve Order
unique = list(dict.fromkeys(my_list))

# Count Occurrences
from collections import Counter

counts = Counter(my_list)
```

<div class="resources">

### Related Tutorials

- [Truth Value Testing in Python](https://realpython.com/search?q=truthy+falsy+python)
- [Conditional Statements and Truthiness](https://realpython.com/search?q=truthiness+conditions+python)
- [Idiomatic Python: EAFP and Truthy Checks](https://realpython.com/search?q=eafp+python)
- [Multiple Assignment and Unpacking](https://realpython.com/search?q=multiple+assignment+python)
- [Flatten Lists in Python (Comprehensions & More)](https://realpython.com/search?q=flatten+list+python)
- [Remove Duplicates From Lists in Python](https://realpython.com/search?q=remove+duplicates+list+python)
- [Counter in Python: Tally Hashable Objects](https://realpython.com/python-counter/)
- [Pythonic Tips & Tricks](https://realpython.com/search?q=pythonic+tricks)

</div>

## 🌎 Virtual Environments

### Create Virtual Environment
```console
$ python -m venv .venv
```

### Activate Virtual Environment
```pscon filename=" 
PS> .venv\Scripts\activate
```

### Activate Virtual
```console filename=" Environment (Linux &"
$ source .venv/bin/activate
```

### Deactivate Virtual
```console filename="
(.venv) $ deactivate
```

<div class="resources">

### Related Tutorials

- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [Manage Multiple Python Environments](https://realpython.com/search?q=virtual+environments+python)
- [Activate and Use Virtual Environments](https://realpython.com/search?q=activate+venv)
- [Virtual Environment Management Tips](https://realpython.com/search?q=deactivate+venv)

</div>

<br class="column-break" />
<br class="column-break" />
<br class="column-break" />

## 📦 Packages

### Install Packages
```console
$ python -m pip install requests
```

### Save Requirements & Install
```console filename=" from
$ python -m pip freeze > requirements.txt
$ python -m pip install -r requirements.txt
```

<div class="resources">

### Related Tutorials

- [What Is `pip`?](https://realpython.com/search?q=what+is+pip)
- [Installing Python Packages](https://realpython.com/search?q=install+packages+pip)
- [Requirements Files in Python Projects](https://realpython.com/search?q=requirements.txt+python)
- [Pinning and Reproducible Environments](https://realpython.com/search?q=pip+freeze)
- [Install From a Requirements File](https://realpython.com/search?q=install+from+requirements.txt)
- [Packaging & Distribution Tutorials](https://realpython.com/tutorials/packaging/)

</div>

## 🌐 Links

### Visit Real Python

- Real Python Search: [realpython.com/search](https://realpython.com/search)
- The Real Python Podcast: [realpython.com/podcasts/](https://realpython.com/podcasts/)
- Common Python Terms: [realpython.com/ref/](https://realpython.com/ref/)
- Learning Paths: [realpython.com/learning-paths/](https://realpython.com/learning-paths/)
- Quizzes and Exercises: [realpython.com/quizzes/](https://realpython.com/quizzes/)
- Code Mentor: [realpython.com/mentor/](https://realpython.com/mentor/)

### Find Real Python on Social Media

- X/Twitter: [x.com/realpython](https://x.com/realpython)
- Instagram: [instagram.com/realpython](https://instagram.com/realpython)
- YouTube: [youtube.com/realpython](https://youtube.com/realpython)
- Facebook: [facebook.com/LearnRealPython](https://facebook.com/LearnRealPython)
- LinkedIn: [linkedin.com/company/realpython-com](https://linkedin.com/company/realpython-com)
- Mastodon: [fosstodon.org/@realpython](https://fosstodon.org/@realpython)

## 💬 Contact

[info@realpython.com](mailto:info@realpython.com)
