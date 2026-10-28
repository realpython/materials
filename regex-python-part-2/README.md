# Regular Expressions: Regexes in Python (Part 2)

This folder provides the code examples for the Real Python tutorial [Regular Expressions: Regexes in Python (Part 2)](https://realpython.com/regex-python-part-2/).

The code uses only Python's standard library and runs on Python 3.6 or later. The output shown in the comments was produced with Python 3.14, so a few representations may look slightly different on older versions.

## Files

Each script runs the tutorial's key examples from one section with `print()` and shows the expected output in a comment below each call:

- [`search_functions.py`](search_functions.py): `re.search()`, `re.match()`, `re.fullmatch()`, `re.findall()`, and `re.finditer()`
- [`substitution_functions.py`](substitution_functions.py): `re.sub()` and `re.subn()` with string and function replacements, backreferences, and `count`
- [`utility_functions.py`](utility_functions.py): `re.split()`, including delimiter capture and `maxsplit`, and `re.escape()`
- [`compiled_regex.py`](compiled_regex.py): `re.compile()`, compiled regex methods with `pos` and `endpos`, and the `.flags`, `.groups`, `.groupindex`, and `.pattern` attributes
- [`match_object_methods.py`](match_object_methods.py): `.group()`, `match[n]`, `.groups()`, `.groupdict()`, `.expand()`, `.start()`, `.end()`, and `.span()`
- [`match_object_attributes.py`](match_object_attributes.py): `.pos`, `.endpos`, `.lastindex`, `.lastgroup`, `.re`, and `.string`

Run any script to see its output:

```sh
$ python search_functions.py
<re.Match object; span=(3, 6), match='123'>
<re.Match object; span=(3, 6), match='FOO'>
None
...
```

You can also import the replacement function `f()` from `substitution_functions.py` to reproduce the tutorial's substitution-by-function examples in the REPL:

```pycon
>>> import re
>>> from substitution_functions import f
>>> re.sub(r"\w+", f, "foo.10.bar.20.baz.30")
'FOO.100.BAR.200.BAZ.300'
>>> re.subn(r"\w+", f, "foo.10.bar.20.baz.30")
('FOO.100.BAR.200.BAZ.300', 6)
```
