# Operator and Function Overloading in Custom Python Classes

This folder provides the code examples for the Real Python tutorial [Operator and Function Overloading in Custom Python Classes](https://realpython.com/operator-function-overloading/).

The code requires Python 3.6 or later and has no third-party dependencies.

## Overloading Built-in Functions

Each of these modules defines the `Order` or `Vector` class from one section of the tutorial:

- `order_len.py`: `Order` with `.__len__()`, so `len()` returns the number of cart items.
- `order_len_float.py`: `Order` whose `.__len__()` returns a `float`, which makes `len()` raise a `TypeError`.
- `vector_abs.py`: `Vector` with `.__abs__()`, so `abs()` returns the vector's magnitude.
- `vector_str.py`: `Vector` with `.__str__()` for a user-friendly `xi+yj` string.
- `vector_repr.py`: `Vector` with `.__repr__()` for a string you can pass to `eval()`.
- `order_bool.py`: `Order` with `.__bool__()`, so an empty order is falsy.

```pycon
>>> from order_len import Order
>>> order = Order(["banana", "apple", "mango"], "Real Python")
>>> len(order)
3

>>> from vector_str import Vector
>>> print(Vector(3, 4))
3i+4j
```

## Overloading Built-in Operators

- `order_add.py`: `Order` with `.__add__()`, so `order + item` returns a new order.
- `order_iadd.py`: `Order` with `.__iadd__()`, so `order += item` updates the order in place.
- `order_iadd_string.py`: `Order` whose `.__iadd__()` returns a string, showing that `+=` rebinds the name to whatever the method returns.
- `order_iadd_none.py`: `Order` whose `.__iadd__()` forgets to return anything, so `order += item` sets `order` to `None`.
- `order_getitem.py`: `Order` with `.__getitem__()` for indexing and slicing the cart.
- `mock.py`: `Mock` with only `.__add__()`, showing that `6 + Mock(5)` raises a `TypeError`.
- `order_radd.py`: `Order` with `.__add__()` and `.__radd__()`, so `item + order` adds the item to the front of the cart.

```pycon
>>> from order_radd import Order
>>> order = Order(["banana", "apple"], "Real Python")
>>> order = "mango" + order
>>> order.cart
['mango', 'banana', 'apple']
```

## A Complete Example

- `custom_complex.py`: The `CustomComplex` class, a complex number that supports `abs()`, `str()`, `repr()`, `+`, `-`, `*`, `**`, `==`, and `!=`.

```pycon
>>> from custom_complex import CustomComplex
>>> a = CustomComplex(1, 2)
>>> b = CustomComplex(3, -4)
>>> a + b
CustomComplex(4, -2)
>>> 3 - a
CustomComplex(2, -2)
>>> b ** 5
CustomComplex(-237, 3116)
```

Run the examples from inside this folder so that Python can import the modules.
