"""Escaping metacharacters with a backslash, and why raw strings help."""

import re

# An unescaped dot is a wildcard, while an escaped dot is literal
print(re.search(".", "foo.bar"))
# <re.Match object; span=(0, 1), match='f'>
print(re.search(r"\.", "foo.bar"))
# <re.Match object; span=(3, 4), match='.'>

s = r"foo\bar"
print(s)
# foo\bar

# Python turns "\\" into a single backslash, which isn't a valid regex
try:
    re.search("\\", s)
except re.error as e:
    print(f"{type(e).__name__}: {e}")
# PatternError: bad escape (end of pattern) at position 0
# (On Python 3.12 and earlier, the exception class is named error.)

# Fix 1: Escape both backslashes in the string literal
print(re.search("\\\\", s))
# <re.Match object; span=(3, 4), match='\\'>

# Fix 2 (cleaner): Use a raw string
print(re.search(r"\\", s))
# <re.Match object; span=(3, 4), match='\\'>
