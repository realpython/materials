# Python 3.11 Demos

This repository holds example code that demos some of the new features in Python 3.11.

## Introduction

You need Python 3.11 installed to run these examples. See the following tutorial instructions:

- [How Can You Install a Pre-Release Version of Python](https://realpython.com/python-pre-release/)

You can learn more about Python 3.11's new features in the following Real Python tutorials:

- [Python 3.11 Preview: Even Better Error Messages](https://realpython.com/python311-error-messages/)
- [Python 3.11 Preview: Task and Exception Groups](https://realpython.com/python311-exception-groups/)
- [Python 3.11 Preview: TOML and `tomllib`](https://realpython.com/python311-tomllib/)

You'll find examples from all these tutorials in this repository.

## Dependencies

Install necessary dependencies for the examples:

```console
$ python -m pip install colorama parse
```

## Examples

This section only contains brief instructions on how you can run the examples. See the tutorials for technical details.

### Improved Error Messages

Load [`scientists.py`](scientists.py) into your interactive REPL:

```console
$ python -i scientists.py 
```
You can then experiment with `dict_to_person()` and `convert_pair()`:

```pycon
>>> dict_to_person(scientists[1])
Traceback (most recent call last):
  ...
  File "/home/realpython/scientists.py", line 37, in dict_to_person
    name=f"{info['name']['first']} {info['name']['last']}",
                                    ~~~~~~~~~~~~^^^^^^^^
KeyError: 'last'

>>> convert_pair(scientists[0], scientists[2])
Traceback (most recent call last):
  ...
  File "/home/realpython/scientists.py", line 44, in convert_pair
    return dict_to_person(first), dict_to_person(second)
                                  ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/realpython/scientists.py", line 38, in dict_to_person
    life_span=(info["birth"]["year"], info["death"]["year"]),
               ~~~~~~~~~~~~~^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

See [Even Better Error Messages in Python 3.11](https://realpython.com/python311-error-messages/#even-better-error-messages-in-python-311) and [PEP 657](https://peps.python.org/pep-0657/).

### Exception Groups

Use `ExceptionGroup` and `except*` to handle several errors at once:

```pycon
>>> try:
...     raise ExceptionGroup(
...         "group", [TypeError("str"), ValueError(654), TypeError("int")]
...     )
... except* ValueError as eg:
...     print(f"Handling ValueErrors: {eg.exceptions}")
...
Handling ValueErrors: (ValueError(654),)
  + Exception Group Traceback (most recent call last):
  |   ...
  | ExceptionGroup: group (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | TypeError: str
    +---------------- 2 ----------------
    | TypeError: int
    +------------------------------------
```

See [Exception Groups and `except*` in Python 3.11](https://realpython.com/python311-exception-groups/#exception-groups-and-except-in-python-311) and [PEP 654](https://peps.python.org/pep-0654/).

### Task Groups

Run [`count.py`](count.py), [`count_gather.py`](count_gather.py), and [`count_taskgroup.py`](count_taskgroup.py) and compare their behaviors. For example:

```console
$ python count_taskgroup.py scientists.py rot13.txt count.py 
scientists.py        □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□ (44)
Files with thirteen lines are too scary!
count.py             □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□ (32)
```

See [Asynchronous Task Groups in Python 3.11](https://realpython.com/python311-exception-groups/#asynchronous-task-groups-in-python-311) and [BPO 46752](https://github.com/python/cpython/pull/31270).

### `tomllib`

[`python_info.toml`](python_info.toml) and [`tomli_pyproject.toml`](tomli_pyproject.toml) show two examples of TOML files.

Use [`read_toml.py`](read_toml.py) to read them:

```console
$ python read_toml.py python_info.toml tomli_pyproject.toml 
======================python_info.toml======================
{'python': {'version': 3.11,
            'release_manager': 'Pablo Galindo Salgado',
            'is_beta': True,
            'beta_release': 3,
            'release_date': datetime.date(2022, 6, 16),
            'peps': [657, 654, 678, 680, 673, 675, 646, 659]}}
====================tomli_pyproject.toml====================
{'build-system': {'requires': ['flit_core>=3.2.0,<4'],
                  'build-backend': 'flit_core.buildapi'},
 'project': {'name': 'tomli',
             'version': '2.0.1',
             'description': "A lil' TOML parser",
             'requires-python': '>=3.7',
             'readme': 'README.md',
             'keywords': ['toml'],
             'urls': {'Homepage': 'https://github.com/hukkin/tomli',
                      'PyPI': 'https://pypi.org/project/tomli'}}}
```

[`tomllib_w.py`](tomllib_w.py) shows how you can write simplified TOML files:

```pycon
>>> import tomllib_w
>>> data = {"url": "https://realpython.com/python311-tomllib/",
...     "author": {"name": "Geir Arne Hjelle", "email": "geirarne@realypython.com"}}

>>> print(tomllib_w.dumps(data))
url = "https://realpython.com/python311-tomllib/"

[author]
name = "Geir Arne Hjelle"
email = "geirarne@realypython.com"
```

See [`tomllib` TOML Parser in Python 3.11](https://realpython.com/python311-tomllib/#tomllib-toml-parser-in-python-311) and [PEP 680](https://peps.python.org/pep-0680/).

### `Self` Type

[`polar_point.py`](polar_point.py) uses `Self` for annotation:

```console
$ python polar_point.py 
PolarPoint(r=5.0, φ=0.9272952180016122)
```

See [`Self` Type](https://realpython.com/python311-tomllib/#self-type) and [PEP 673](https://peps.python.org/pep-0673/).

### Arbitrary `LiteralString` Type

[`execute_sql.py`](execute_sql.py) shows an example of `LiteralString`:

```console
$ python execute_sql.py 
Pretending to execute: SELECT * FROM users
Pretending to execute: SELECT * FROM users

Enter table name: users; DROP TABLE users; --
Pretending to execute: SELECT * FROM users; DROP TABLE users; --
```

See [Arbitrary Literal String Type](https://realpython.com/python311-tomllib/#arbitrary-literal-string-type) and [PEP 675](https://peps.python.org/pep-0675/).

### Variadic Generic Types: `TypeVarTuple`

[`ndarray.py`](ndarray.py) shows an example of using `TypeVarTuple`.

See [Variadic Generic Types](https://realpython.com/python311-tomllib/#variadic-generic-types) and [PEP 646](https://peps.python.org/pep-0646/).

### Exception Annotations

Use `.add_notes()` to annotate exceptions with custom notes:

```pycon
>>> err = ValueError(678)
>>> err.add_note("Enriching Exceptions with Notes")
>>> err.add_note("Python 3.11")

>>> err.__notes__
['Enriching Exceptions with Notes', 'Python 3.11']
>>> for note in err.__notes__:
...     print(note)
...
Enriching Exceptions with Notes
Python 3.11

>>> raise err
Traceback (most recent call last):
  ...
ValueError: 678
Enriching Exceptions with Notes
Python 3.11
```

See [Annotate Exceptions With Custom Notes](https://realpython.com/python311-exception-groups/#annotate-exceptions-with-custom-notes) and [PEP 678](https://peps.python.org/pep-0678/).

### Reference Active Exceptions

You can use `sys.exception()` to access the active exception:

```pycon
>>> import sys

>>> try:
...     raise ValueError("bpo-46328")
... except ValueError:
...     print(f"Handling {sys.exception()}")
...
Handling bpo-46328
```

Note that this is typically not necessary in regular code. You can use the `except ValueError as err` syntax instead.

See [Reference the Active Exception With `sys.exception()`](https://realpython.com/python311-exception-groups/#reference-the-active-exception-with-sysexception) and [BPO 46328](https://github.com/python/cpython/issues/90486).

### Consistent Tracebacks

`traceback_demo.py` shows that tracebacks can be consistently accessed through the exception object:

```console
$ python traceback_demo.py 
tb_last(exc_value.__traceback__) = 'bad_calculation:13'
tb_last(exc_tb)                  = 'bad_calculation:13'
```

See [Reference the Active Traceback Consistently](https://realpython.com/python311-exception-groups/#reference-the-active-traceback-consistently) and [BPO 45711](https://github.com/python/cpython/issues/89874).

### New Math Functions: `cbrt()` and `exp2()`

You can use `math.cbrt()` to calculate cube roots:

```pycon
>>> import math
>>> math.cbrt(729)
9.000000000000002

>>> 729**(1/3)
8.999999999999998

>>> math.pow(729, 1/3)
8.999999999999998
```

You can use `math.exp2()` to calculate powers of two:

```pycon
>>> import math
>>> math.exp2(16)
65536.0

>>> 2**16
65536

>>> math.pow(2, 16)
65536.0
```

See [Cube Roots and Powers of Two](https://realpython.com/python311-error-messages/#cube-roots-and-powers-of-two), [BPO 44357](https://github.com/python/cpython/issues/88523) and [BPO 45917](https://github.com/python/cpython/issues/90075).

### Underscores in Fractions

You can use underscores when defining fractions from strings:

```pycon
>>> from fractions import Fraction
>>> print(Fraction("6_024/1_729"))
6024/1729
```

See [Underscores in Fractions](https://realpython.com/python311-error-messages/#underscores-in-fractions) and [BPO 44258](https://github.com/python/cpython/issues/88424).

### Flexible Calling of Objects: `operator.call()`

The Norwegian calculator implemented in [`kalkulator.py`](kalkulator.py) uses `operator.call()`:

```pycon
>>> import kalkulator
>>> kalkulator.calculate("20 pluss 22")
42.0

>>> kalkulator.calculate("11 delt på 3")
3.6666666666666665
```

See [Flexible Calling of Objects](https://realpython.com/python311-error-messages/#flexible-calling-of-objects) and [BPO 44019](https://github.com/python/cpython/issues/88185).

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
