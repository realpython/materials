# Dealing With Exceptions

## What is an Exception?

An **Exception** gets **raised** when code encounters an occasional,
but not unexpected, error. Although exceptions are an unavoidable
part of software, because you are aware that exceptions may occur,
you should write code to deal with or **handle** them.
Unhandled exceptions will cause a program to crash.

## How Do You Handle Them?

You implement [*exception handling*](https://realpython.com/python-exceptions/)
to handle exceptions. In its most basic form, this provides both a *try*
and one or more *except* blocks:

* The *try* block contains the code you wish to monitor for exceptions.
Any exceptions raised within *try* will be elligible for handling.

* One or more *except* blocks are where you define code that will run
when exceptions occur and handle them.
This is how you stop the exception from crashing the code.

## What Are Some Common Exceptions

The Python language supports more than sixty common exceptions.
Two of the more common are:


| Exception | Cause |
|:- |:- |
| **ZeroDivisionError** | Raised when you attempt to divide by zero |
| **ValueError** | Raised when you pass an inappropriate value |

## Example

```python
try:
    first_number = float(input("Enter your first number"))
    second_number = float(input("Enter your second number"))
    print(f"{first_number} / {second_number} = {first_number / second_number}")
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You must supply a number")
```
