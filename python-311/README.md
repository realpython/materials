# Python 3.11 Demos

![Python 3.11: Cool New Features for You to Try](python-311.png)

This repository holds example code that demos some of the new features in Python 3.11.

## Introduction

You need Python 3.11 installed to run these examples. See the following tutorial instructions:

- [How Can You Install a Pre-Release Version of Python](https://realpython.com/python-pre-release/)

You can learn more about Python 3.11's new features in the following Real Python tutorials:

- [Python 3.11 Preview: Even Better Error Messages](https://realpython.com/python311-error-messages/)
- [Python 3.11 Preview: Task and Exception Groups](https://realpython.com/python311-exception-groups/)
- [Python 3.11 Preview: TOML and `tomllib`](https://realpython.com/python311-tomllib/)
- [Python 3.11: Cool New Features for You to Try](https://realpython.com/python311-new-features/)

You'll find examples from all these tutorials in this repository.

## Dependencies

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/):

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install necessary dependencies for the examples (see [`requirements.in`](requirements.in)):

```console
(venv) $ python -m pip install aiohttp colorama parse python-magic
```

Alternatively, you can install dependencies from [`requirements.txt`](requirements.txt) if you want to ensure that you're using the same versions of the third-party packages:

```console
(venv) $ python -m pip install -r requirements.txt
```

> **Note:** `python-magic` depends on a C library that you may need to install on your system. See the [documentation](https://github.com/ahupp/python-magic#installation) for details.

These examples have been run with [Python 3.11.0rc1](https://www.python.org/downloads/release/python-3110rc1/), the first release candidate of Python 3.11.

## Examples

This section only contains brief instructions on how you can run the examples. See the tutorials for technical details.

### Improved Error Messages

Run [`inverse.py](inverse.py) for a quick look at the improved tracebacks:

```console
(venv) $ python inverse.py 
Traceback (most recent call last):
  File "/home/realpython/inverse.py", line 5, in <module>
    print(inverse(0))
          ^^^^^^^^^^
  File "/home/realpython/inverse.py", line 2, in inverse
    return 1 / number
           ~~^~~~~~~~
ZeroDivisionError: division by zero
```

The `scientists.py` and `programmers.py` show two different versions of the same kind of example.

For example, load [`scientists.py`](scientists.py) into your interactive REPL:

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

See [Even Better Error Messages in Python 3.11](https://realpython.com/python311-error-messages/#even-better-error-messages-in-python-311), [More Informative Error Tracebacks](https://realpython.com/python311-new-features/#more-informative-error-tracebacks), and [PEP 657](https://peps.python.org/pep-0657/).

### Specializing Adaptive Interpreter

The interpreter will specialize bytecodes that are run often. This is part of the Faster CPython project. Note how the bytecodes change as the program is running:

```console
(venv) $ python specialized.py 

 ============================ Before any invocation ============================
  8           0 RESUME                   0

  9           2 LOAD_CONST               1 (0.3048)
              4 LOAD_FAST                0 (feet)
              6 BINARY_OP                5 (*)
             10 RETURN_VALUE

 ========================== After 7 float invocations ==========================
  8           0 RESUME                   0

  9           2 LOAD_CONST               1 (0.3048)
              4 LOAD_FAST                0 (feet)
              6 BINARY_OP                5 (*)
             10 RETURN_VALUE

 ========================== After 8 float invocations ==========================
  8           0 RESUME_QUICK             0

  9           2 LOAD_CONST__LOAD_FAST     1 (0.3048)
              4 LOAD_FAST                0 (feet)
              6 BINARY_OP_MULTIPLY_FLOAT     5 (*)
             10 RETURN_VALUE

 ===================== After 8 float and 52 int invocations ====================
  8           0 RESUME_QUICK             0

  9           2 LOAD_CONST__LOAD_FAST     1 (0.3048)
              4 LOAD_FAST                0 (feet)
              6 BINARY_OP_MULTIPLY_FLOAT     5 (*)
             10 RETURN_VALUE

 ===================== After 8 float and 53 int invocations ====================
  8           0 RESUME_QUICK             0

  9           2 LOAD_CONST__LOAD_FAST     1 (0.3048)
              4 LOAD_FAST                0 (feet)
              6 BINARY_OP_ADAPTIVE       5 (*)
             10 RETURN_VALUE
```

See [Faster Code Execution](https://realpython.com/python311-new-features/#faster-code-execution) and [PEP 659](https://peps.python.org/pep-0659/).

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

See [Exception Groups and `except*` in Python 3.11](https://realpython.com/python311-exception-groups/#exception-groups-and-except-in-python-311), [Exception Groups](https://realpython.com/python311-new-features/#exception-groups), and [PEP 654](https://peps.python.org/pep-0654/).

### Task Groups

Run [`count.py`](count.py), [`count_gather.py`](count_gather.py), and [`count_taskgroup.py`](count_taskgroup.py) and compare their behaviors. For example:

```console
(venv) $ python count_taskgroup.py scientists.py rot13.txt count.py 
scientists.py        □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□ (44)
Files with thirteen lines are too scary!
count.py             □□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□ (32)
```

See [Asynchronous Task Groups in Python 3.11](https://realpython.com/python311-exception-groups/#asynchronous-task-groups-in-python-311) and [gh-31270](https://github.com/python/cpython/pull/31270).

For a different example, have a look at [`download_peps_gather.py`](download_peps_gather.py) and [`download_peps_taskgroup.py](download_peps_taskgroup.py). For example:

```console
(venv) $ python download_peps_taskgroup.py 
Downloading PEP 492
Downloading PEP 525
Downloading PEP 530
Downloading PEP 3148
Downloading PEP 3156
Downloaded PEP 492: Coroutines with async and await syntax
Downloaded PEP 530: Asynchronous Comprehensions
Downloaded PEP 525: Asynchronous Generators
Downloaded PEP 3148: futures - execute computations asynchronously
Downloaded PEP 3156: Asynchronous IO Support Rebooted: the "asyncio" Module
```

See [Nicer Syntax for Asynchronous Tasks](https://realpython.com/python311-new-features/#nicer-syntax-for-asynchronous-tasks).

### `tomllib`

[`python_info.toml`](python_info.toml), [`tomli_pyproject.toml`](tomli_pyproject.toml), and [`units.toml`](units.toml) show three examples of TOML files.

Use [`read_toml.py`](read_toml.py) to read them:

```console
(venv) $ python read_toml.py python_info.toml tomli_pyproject.toml units.toml 
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
=========================units.toml=========================
{'second': {'label': {'singular': 'second', 'plural': 'seconds'},
            'aliases': ['s', 'sec', 'seconds']},
 'minute': {'label': {'singular': 'minute', 'plural': 'minutes'},
            'aliases': ['min', 'minutes'],
            'multiplier': 60,
            'to_unit': 'second'},
 'hour': {'label': {'singular': 'hour', 'plural': 'hours'},
          'aliases': ['h', 'hr', 'hours'],
          'multiplier': 60,
          'to_unit': 'minute'},
 'day': {'label': {'singular': 'day', 'plural': 'days'},
         'aliases': ['d', 'days'],
         'multiplier': 24,
         'to_unit': 'hour'},
 'year': {'label': {'singular': 'year', 'plural': 'years'},
          'aliases': ['y', 'yr', 'years', 'julian_year', 'julian years'],
          'multiplier': 365.25,
          'to_unit': 'day'}}
```

You can use [`tomllib_w.py`](tomllib_w.py) to write simplified TOML files. [`write_toml.py`](write_toml.py) demonstrates how you can use it:

```console
(venv) $ python write_toml.py 
url = "https://realpython.com/python311-tomllib/"

[author]
name = "Geir Arne Hjelle"
email = "geirarne@realpython.com"
```

You can see an example of using a TOML file to set up a flexible unit converter in [`units.py`](units.py).

See [`tomllib` TOML Parser in Python 3.11](https://realpython.com/python311-tomllib/#tomllib-toml-parser-in-python-311), [Support for TOML Configuration Parsing](https://realpython.com/python311-new-features/#support-for-toml-configuration-parsing), and [PEP 680](https://peps.python.org/pep-0680/).

### `Self` Type

[`polar_point.py`](polar_point.py) and [`programmers.py`](programmers.py) uses `Self` for annotation:

```console
(venv) $ python polar_point.py 
PolarPoint(r=5.0, φ=0.9272952180016122)
```

See [`Self` Type](https://realpython.com/python311-tomllib/#self-type), [Improved Type Variables](https://realpython.com/python311-new-features/#improved-type-variables), and [PEP 673](https://peps.python.org/pep-0673/).

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

[`ndarray.py`](ndarray.py) and [`tuple_order.py`](tuple_order.py) show examples of using `TypeVarTuple`.

See [Variadic Generic Types](https://realpython.com/python311-tomllib/#variadic-generic-types), [Improved Type Variables](https://realpython.com/python311-new-features/#improved-type-variables), and [PEP 646](https://peps.python.org/pep-0646/).

### Zero-Cost Exceptions

The internal handling of exceptions has been restructured. Exception handling is now done with a jump-table:

```console
(venv) $ python zero_cost_exceptions.py 
  4           0 RESUME                   0

  5           2 NOP

  6           4 LOAD_CONST               1 (1)
              6 LOAD_FAST                0 (number)
              8 BINARY_OP               11 (/)
             12 RETURN_VALUE
        >>   14 PUSH_EXC_INFO

  7          16 LOAD_GLOBAL              0 (ZeroDivisionError)
             28 CHECK_EXC_MATCH
             30 POP_JUMP_FORWARD_IF_FALSE    19 (to 70)
             32 POP_TOP

  8          34 LOAD_GLOBAL              3 (NULL + print)
             46 LOAD_CONST               2 ('0 has no inverse')
             48 PRECALL                  1
             52 CALL                     1
             62 POP_TOP
             64 POP_EXCEPT
             66 LOAD_CONST               0 (None)
             68 RETURN_VALUE

  7     >>   70 RERAISE                  0
        >>   72 COPY                     3
             74 POP_EXCEPT
             76 RERAISE                  1
ExceptionTable:
  4 to 10 -> 14 [0]
  14 to 62 -> 72 [1] lasti
  70 to 70 -> 72 [1] lasti
```

See [Zero-Cost Exceptions](https://realpython.com/python311-new-features/#zero-cost-exceptions) and [gh-84403](https://github.com/python/cpython/issues/84403).

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

You can use exception notes to add context to errors raised by your program. For example, [`timestamped_errors.py`](timestamped_errors.py) adds a timestamp to an error:

```console
(venv)  python timestamped_errors.py 
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
Raised at 2022-10-18 12:28:55.447764
```

See [Annotate Exceptions With Custom Notes](https://realpython.com/python311-exception-groups/#annotate-exceptions-with-custom-notes), [Exception Notes](https://realpython.com/python311-new-features/#exception-notes), and [PEP 678](https://peps.python.org/pep-0678/).

### Reference Active Exceptions

You can use `sys.exception()` to access the active exception:

```console
(venv) $ python active_exception.py 
Handling gh-90486
Handling gh-90486
```

Note that this is typically not necessary in regular code. You can use the `except ValueError as err` syntax instead.

See [Reference the Active Exception With `sys.exception()`](https://realpython.com/python311-exception-groups/#reference-the-active-exception-with-sysexception) and [gh-90486](https://github.com/python/cpython/issues/90486).

### Consistent Tracebacks

`traceback_demo.py` shows that tracebacks can be consistently accessed through the exception object:

```console
(venv) $ python traceback_demo.py 
tb_last(exc_value.__traceback__) = 'bad_calculation:13'
tb_last(exc_tb)                  = 'bad_calculation:13'
```

See [Reference the Active Traceback Consistently](https://realpython.com/python311-exception-groups/#reference-the-active-traceback-consistently) and [gh-89874](https://github.com/python/cpython/issues/89874).

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

See [Cube Roots and Powers of Two](https://realpython.com/python311-error-messages/#cube-roots-and-powers-of-two), [gh-88523](https://github.com/python/cpython/issues/88523) and [gh-90075](https://github.com/python/cpython/issues/90075).

### Underscores in Fractions

You can use underscores when defining fractions from strings:

```console
(venv) $ python underscore.py 
Fraction('6_024/1_729') = 6024/1729
```

See [Underscores in Fractions](https://realpython.com/python311-error-messages/#underscores-in-fractions) and [gh-88424](https://github.com/python/cpython/issues/88424).

### Flexible Calling of Objects: `operator.call()`

The Norwegian calculator implemented in [`kalkulator.py`](kalkulator.py) uses `operator.call()`:

```console
(venv) $ python kalkulator.py 
20 pluss 22 = 42.0
2022 minus 1991 = 31.0
45 ganger 45 = 2025.0
11 delt på 3 = 3.6666666666666665
```

See [Flexible Calling of Objects](https://realpython.com/python311-error-messages/#flexible-calling-of-objects) and [gh-88185](https://github.com/python/cpython/issues/88185).

### Dead Batteries

Some of the less used standard libraries have started raising deprecation warnings. If you happen to be using them, you should look for more modern alternatives.

For example, [`dead_imghdr.py`](dead_imghdr.py) shows the warning raised by importing `imghdr` and how to use [python-magic](https://pypi.org/project/python-magic/) as an alternative:

```console
(venv) $ python dead_imghdr.py 
/home/realpython/dead_imghdr.py:1: DeprecationWarning: 'imghdr' is deprecated and slated for removal in Python 3.13
  import imghdr
jpeg
JPEG image data, JFIF standard 1.02, aspect ratio, density 100x100, segment length 16, progressive, precision 8, 1920x1080, components 3
```

See [Dead Batteries](https://realpython.com/python311-new-features/#dead-batteries) and [PEP 594](https://peps.python.org/pep-0594/).

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
