# Understanding the Python Mock Object Library

This folder contains code examples related to the RealPython tutorial on [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/).

The example code showcases some of the different use cases of `unittest.mock` in a single test file, `test_holidays.py`. When writing your own tests, keep in mind that readability counts and that your test code will be more readable if you keep one consistent approach to mocking.

## Installation

1. Create a Python virtual environment

```sh
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the requirements

```sh
(venv) $ pip install requests
```

## Run the Tests

```sh
(venv) $ python test_holidays.py
```

All the tests should pass. Go ahead and play with the code examples, change them, break them, and practice your understanding of using `unittest.mock` for testing in Python.

## About the Author

Martin Breuss - Email: martin@realpython.com

## License

Distributed under the MIT license. See `LICENSE` for more information.
