# calc

Calc is a CLI application that performs arithmetic operations. It takes a subcommand representing the target operation and two numeric arguments. It returns the result of performing the target operations between the two input values.

## Installation

1. Create a Python virtual environment

```sh
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install calc in editable mode

```sh
(venv) $ python -m pip install -e .
```

## Run the Project

```sh
(venv) $ calc add 3 4
7.0

(venv) $ calc sub 3 4
-1.0

(venv) $ calc mul 3 4
12.0

(venv) $ calc div 3 4
0.75
```

## Features

Calc currently provides the following options:

- `add` takes two numbers and adds them together.
- `sub` takes two numbers and subtracts them.
- `mul` takes two numbers and multiplies them.
- `div` takes two numbers and divides them.

## About the Author

Leodanis Pozo Ramos - Email: leodanis@realpython.com

## License

Distributed under the MIT license. See `LICENSE` in the root directory of this `materials` repo for more information.
