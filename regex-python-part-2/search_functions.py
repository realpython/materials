"""Searching functions: re.search(), re.match(), re.fullmatch(),
re.findall(), and re.finditer().
"""

import re

# re.search() scans a string for a regex match
print(re.search(r"(\d+)", "foo123bar"))
# <re.Match object; span=(3, 6), match='123'>
print(re.search(r"[a-z]+", "123FOO456", flags=re.IGNORECASE))
# <re.Match object; span=(3, 6), match='FOO'>
print(re.search(r"\d+", "foo.bar"))
# None

# re.match() only matches at the beginning of the string
print(re.search(r"\d+", "123foobar"))
# <re.Match object; span=(0, 3), match='123'>
print(re.search(r"\d+", "foo123bar"))
# <re.Match object; span=(3, 6), match='123'>
print(re.match(r"\d+", "123foobar"))
# <re.Match object; span=(0, 3), match='123'>
print(re.match(r"\d+", "foo123bar"))
# None

# MULTILINE affects re.search() but not re.match()
s = "foo\nbar\nbaz"
print(re.search("^foo", s))
# <re.Match object; span=(0, 3), match='foo'>
print(re.search("^bar", s, re.MULTILINE))
# <re.Match object; span=(4, 7), match='bar'>
print(re.match("^foo", s))
# <re.Match object; span=(0, 3), match='foo'>
print(re.match("^bar", s, re.MULTILINE))
# None

# re.fullmatch() matches only if the regex matches the entire string
print(re.fullmatch(r"\d+", "123foo"))
# None
print(re.fullmatch(r"\d+", "foo123"))
# None
print(re.fullmatch(r"\d+", "foo123bar"))
# None
print(re.fullmatch(r"\d+", "123"))
# <re.Match object; span=(0, 3), match='123'>
print(re.search(r"^\d+$", "123"))
# <re.Match object; span=(0, 3), match='123'>

# re.findall() returns a list of all non-overlapping matches
print(re.findall(r"\w+", "...foo,,,,bar:%$baz//|"))
# ['foo', 'bar', 'baz']
print(re.findall(r"#(\w+)#", "#foo#.#bar#.#baz#"))
# ['foo', 'bar', 'baz']
print(re.findall(r"(\w+),(\w+)", "foo,bar,baz,qux,quux,corge"))
# [('foo', 'bar'), ('baz', 'qux'), ('quux', 'corge')]
print(re.findall(r"(\w+),(\w+),(\w+)", "foo,bar,baz,qux,quux,corge"))
# [('foo', 'bar', 'baz'), ('qux', 'quux', 'corge')]

# re.finditer() returns an iterator that yields match objects
it = re.finditer(r"\w+", "...foo,,,,bar:%$baz//|")
print(next(it))
# <re.Match object; span=(3, 6), match='foo'>
print(next(it))
# <re.Match object; span=(10, 13), match='bar'>
print(next(it))
# <re.Match object; span=(16, 19), match='baz'>
print(next(it, "StopIteration"))  # A bare next(it) raises StopIteration
# StopIteration

for i in re.finditer(r"\w+", "...foo,,,,bar:%$baz//|"):
    print(i)
# <re.Match object; span=(3, 6), match='foo'>
# <re.Match object; span=(10, 13), match='bar'>
# <re.Match object; span=(16, 19), match='baz'>
