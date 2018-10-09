"""Examples using decorators

See https://realpython.com/primer-on-python-decorators/

This file contains code for many of the examples in the text. You can
find the decorators themselves in the decorators.py file.
"""

from datetime import datetime
import functools
import math
import random

from decorators import (
    cache,
    count_calls,
    debug,
    do_twice,
    PLUGINS,
    register,
    set_unit,
    singleton,
    slow_down,
    timer,
)


# First-Class Objects
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


# Returning Functions From Functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


# Simple Decorators
def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep.

    return wrapper


# Syntactic Sugar!
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


# Reusing Decorators
@do_twice
def say_whee_twice():
    print("Whee!")


# Returning Values From Decorated Functions
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


# A Few Real World Examples
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before.
        value = func(*args, **kwargs)
        # Do something after.
        return value

    return wrapper_decorator


# Timing Functions
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


# Debugging Code
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


# Slowing Down Code (Revisited)
@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


# Registering Plugins
#
# The names of the plugins have been changed from the text to avoid name
# clashes with earlier examples
@register
def say_hi(name):
    return f"Hi {name}"


@register
def be_cool(name):
    return f"Yo {name}, together we are the coolest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


# Example Using Built-in Class Decorators
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius ** 2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.141_592_653_5


# Decorating Classes
class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


# Nesting Decorators
@do_twice
@debug
def greet(name):
    print(f"Hello {name}")


# Creating Singletons
@singleton
class TheOne:
    pass


# Caching Return Values
@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@functools.lru_cache(maxsize=4)  # lru_cache is preferred to rolling your own
def fibonacci_lru(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


# Adding Information About Units
@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius ** 2 * height
