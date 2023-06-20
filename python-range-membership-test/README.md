# Why Are Membership Tests So Fast for `range()` in Python?

This repository holds the code for Real Python's [Why Are Membership Tests So Fast for `range()` in Python?](https://realpython.com/python-range-membership-test/) tutorial.

In [`range_tools.py`](range_tools.py), you'll find an implementation of a custom `Range` class that behaves similarly to the built-in `range()`:

```pycon
>>> from range_tools import Range

>>> Range(start=1, stop=10, step=2)
Range(start=1, stop=10, step=2)

>>> list(Range(start=1, stop=10, step=2))
[1, 3, 5, 7, 9]
```

While `range()` is implemented in C, you can look at the source code of `Range` to get an idea of how `range()` works under the hood.

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
