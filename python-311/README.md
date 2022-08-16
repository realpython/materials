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

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/):

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install necessary dependencies for the examples (see [`requirements.in`](requirements.in)):

```console
(venv) $ python -m pip install colorama parse
```

Alternatively, you can install dependencies from [`requirements.txt`](requirements.txt) if you want to ensure that you're using the same versions of the third-party packages:

```console
(venv) $ python -m pip install -r requirements.txt
```

These examples have been run with [Python 3.11.0rc1](https://www.python.org/downloads/release/python-3110rc1/), the first release candidate of Python 3.11.

## Examples

This section only contains brief instructions on how you can run the examples. See the tutorials for technical details.

### Improved Error Messages

Load [`scientists.py`](scientists.py) into your interactive REPL:

```console
(venv) $ python -i scientists.py 
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

```console
(venv) $ python exception_group.py 
Handling ValueErrors: (ValueError(654),)
  + Exception Group Traceback (most recent call last):
  |   File "/home/realpython/exception_group.py", line 2, in <module>
  |     raise ExceptionGroup(
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
(venv) $ python count_taskgroup.py scientists.py rot13.txt count.py 
scientists.py        □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□ (44)
Files with thirteen lines are too scary!
count.py             □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□ (32)
```

See [Asynchronous Task Groups in Python 3.11](https://realpython.com/python311-exception-groups/#asynchronous-task-groups-in-python-311) and [BPO 46752](https://github.com/python/cpython/pull/31270).

### `tomllib`

[`python_info.toml`](python_info.toml) and [`tomli_pyproject.toml`](tomli_pyproject.toml) show two examples of TOML files.

Use [`read_toml.py`](read_toml.py) to read them:

```console
(venv) $ python read_toml.py python_info.toml tomli_pyproject.toml 
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

You can use [`tomllib_w.py`](tomllib_w.py) to write simplified TOML files. [`write_toml.py`](write_toml.py) demonstrates how you can use it:

```console
(venv) $ python write_toml.py 
url = "https://realpython.com/python311-tomllib/"

[author]
name = "Geir Arne Hjelle"
email = "geirarne@realpython.com"
```

See [`tomllib` TOML Parser in Python 3.11](https://realpython.com/python311-tomllib/#tomllib-toml-parser-in-python-311) and [PEP 680](https://peps.python.org/pep-0680/).

### `Self` Type

[`polar_point.py`](polar_point.py) uses `Self` for annotation:

```console
(venv) $ python polar_point.py 
PolarPoint(r=5.0, φ=0.9272952180016122)
```

See [`Self` Type](https://realpython.com/python311-tomllib/#self-type) and [PEP 673](https://peps.python.org/pep-0673/).

### Arbitrary `LiteralString` Type

[`execute_sql.py`](execute_sql.py) shows an example of `LiteralString`:

```console
(venv) $ python execute_sql.py 
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

```console
(venv) $ python exception_notes.py 
err.__notes__ = ['Enriching Exceptions with Notes', 'Python 3.11']

--------------------- Loop over notes ----------------------
Enriching Exceptions with Notes
Python 3.11

--------------- Notes are added to traceback ---------------
Traceback (most recent call last):
  File "/home/realpython/exception_notes.py", line 12, in <module>
    raise err
ValueError: 678
Enriching Exceptions with Notes
Python 3.11
```

See [Annotate Exceptions With Custom Notes](https://realpython.com/python311-exception-groups/#annotate-exceptions-with-custom-notes) and [PEP 678](https://peps.python.org/pep-0678/).

### Reference Active Exceptions

You can use `sys.exception()` to access the active exception:

```console
(venv) $ python active_exception.py 
Handling bpo-46328
Handling bpo-46328
```

Note that this is typically not necessary in regular code. You can use the `except ValueError as err` syntax instead.

See [Reference the Active Exception With `sys.exception()`](https://realpython.com/python311-exception-groups/#reference-the-active-exception-with-sysexception) and [BPO 46328](https://github.com/python/cpython/issues/90486).

### Consistent Tracebacks

`traceback_demo.py` shows that tracebacks can be consistently accessed through the exception object:

```console
(venv) $ python traceback_demo.py 
tb_last(exc_value.__traceback__) = 'bad_calculation:13'
tb_last(exc_tb)                  = 'bad_calculation:13'
```

See [Reference the Active Traceback Consistently](https://realpython.com/python311-exception-groups/#reference-the-active-traceback-consistently) and [BPO 45711](https://github.com/python/cpython/issues/89874).

### New Math Functions: `cbrt()` and `exp2()`

You can use `math.cbrt()` to calculate cube roots:

```console
(venv) $ python cube_root.py 
math.cbrt(729) = 9.000000000000002
729 ** (1 / 3) = 8.999999999999998
math.pow(729, 1 / 3) = 8.999999999999998
```

You can use `math.exp2()` to calculate powers of two:

```console
(venv) $ python power_of_two.py 
math.exp2(16) = 65536.0
2**16 = 65536
math.pow(2, 16) = 65536.0
```

See [Cube Roots and Powers of Two](https://realpython.com/python311-error-messages/#cube-roots-and-powers-of-two), [BPO 44357](https://github.com/python/cpython/issues/88523) and [BPO 45917](https://github.com/python/cpython/issues/90075).

### Underscores in Fractions

You can use underscores when defining fractions from strings:

```console
(venv) $ python underscore.py 
Fraction('6_024/1_729') = 6024/1729
```

See [Underscores in Fractions](https://realpython.com/python311-error-messages/#underscores-in-fractions) and [BPO 44258](https://github.com/python/cpython/issues/88424).

### Flexible Calling of Objects: `operator.call()`

The Norwegian calculator implemented in [`kalkulator.py`](kalkulator.py) uses `operator.call()`:

```console
(venv) $ python kalkulator.py 
20 pluss 22 = 42.0
2022 minus 1991 = 31.0
45 ganger 45 = 2025.0
11 delt på 3 = 3.6666666666666665
```

See [Flexible Calling of Objects](https://realpython.com/python311-error-messages/#flexible-calling-of-objects) and [BPO 44019](https://github.com/python/cpython/issues/88185).

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
