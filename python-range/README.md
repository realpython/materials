# Python `range()`: Represent Numerical Ranges

This repository holds the code for Real Python's [Python `range()`: Represent Numerical Ranges](https://realpython.com/python-range/) tutorial.

## reverse_range()

In [`reverse_range.py`](reverse_range.py), you can find an explicit implementation of a function that can reverse a general range.

```python
>>> from reverse_range import reverse_range

>>> reverse_range(range(1, 20, 4))
range(17, 0, -4)

>>> list(reverse_range(range(1, 20, 4)))
[17, 13, 9, 5, 1]
```

In practical applications, you should use `reversed(range(1, 20, 4))` or `range(1, 20, 4)[::-1]` instead.

## PiDigits

The file [`pi_digits.py`](pi_digits.py) shows the implementation of `PiDigits` which is an integer-like type that can be used as arguments to `range()`:

```python
>>> from pi_digits import PiDigits

>>> PiDigits(3)
PiDigits(num_digits=3)

>>> int(PiDigits(3))
314

>>> range(PiDigits(3))
range(0, 314)
```

See [the tutorial](https://realpython.com/python-range/#create-a-range-using-integer-like-parameters) for more details.

## FloatRange

In [`float_range.py`](float_range.py), you'll find an implementation of a custom `FloatRange` class that behaves similarly to the built-in `range()` except that its arguments can be floating point numbers:

```pycon
>>> from float_range import FloatRange

>>> FloatRange(1, 10, 1.2)
FloatRange(start=1, stop=10, step=1.2)

>>> list(FloatRange(1, 10, 1.2))
[1.0, 2.2, 3.4, 4.6, 5.8, 7.0, 8.2, 9.4]
```

The built-in `range()` is implemented in C. However, you can look at the source code of `FloatRange` to get an idea of how `range()` works under the hood.

If you need to work with floating-point ranges, you can use `FloatRange`. However, NumPy's [`arange()`](https://realpython.com/how-to-use-numpy-arange/) will give you better performance, and is probably a better option overall.

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
