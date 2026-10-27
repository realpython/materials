# Regular Expressions: Regexes in Python (Part 1)

This folder provides the code examples for the Real Python tutorial [Regular Expressions: Regexes in Python (Part 1)](https://realpython.com/regex-python/).

Each script runs the tutorial's key `re.search()` examples for one section. Every `print()` call is followed by a comment showing the output you'll see, so you can read the files like the tutorial's REPL sessions or run them to check the results yourself.

## Files

- `search_basics.py`: Two ways to import `re.search()`, a first pattern-matching example, and a first look at character classes and the dot wildcard
- `single_character.py`: Metacharacters that match a single character: `[]`, `.`, `\w`, `\W`, `\d`, `\D`, `\s`, and `\S`
- `escaping.py`: Escaping metacharacters with a backslash, and why raw strings are cleaner
- `anchors.py`: The `^`, `\A`, `$`, `\Z`, `\b`, and `\B` anchors
- `quantifiers.py`: The `*`, `+`, `?`, `{m}`, and `{m,n}` quantifiers and their non-greedy versions
- `grouping.py`: Groups, capturing with `.groups()` and `.group()`, numbered and named backreferences, non-capturing groups, and conditional matches
- `lookarounds.py`: Positive and negative lookahead and lookbehind assertions
- `alternation.py`: Inline comments with `(?#...)` and alternation with `|`
- `flags.py`: The `IGNORECASE`, `MULTILINE`, `DOTALL`, `VERBOSE`, `ASCII`, and `UNICODE` flags, combining flags, and setting or clearing flags inside a regex
- `debug_flag.py`: Inspecting how the parser reads a regex with `re.DEBUG`

## Usage

Run any script with Python:

```console
$ python anchors.py
<re.Match object; span=(0, 3), match='foo'>
None
<re.Match object; span=(0, 3), match='foo'>
None
...
```

Since Python 3.8, `re.DEBUG` prints the parse tree followed by a blank line and a dump of the compiled pattern. `debug_flag.py` prints only the parse tree, which is the part the tutorial discusses.

## Requirements

The code uses only the standard library and needs Python 3.7 or later. The outputs in the comments come from Python 3.14. On Python 3.12 and earlier, regex errors show up as `error` instead of `PatternError`, and before Python 3.11, a global flag such as `(?s)` that isn't at the start of a regex only triggers a `DeprecationWarning` instead of an error.
