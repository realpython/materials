"""Importing re.search() and a first look at pattern matching with it."""

# Approach 1: Import the module and use the module name as a prefix
import re

# Approach 2: Import the function by name
from re import search

print(re.search("123", "foo123bar"))
# <re.Match object; span=(3, 6), match='123'>
print(search("123", "foo123bar"))
# <re.Match object; span=(3, 6), match='123'>

# First pattern-matching example
s = "foo123bar"
print(re.search("123", s))
# <re.Match object; span=(3, 6), match='123'>

# A match object is truthy
if re.search("123", s):
    print("Found a match.")
else:
    print("No match.")
# Found a match.

# span=(3, 6) means the same thing as slice notation
print(repr(s[3:6]))
# '123'

# A character class matches any single character inside the brackets
print(re.search("[0-9][0-9][0-9]", s))
# <re.Match object; span=(3, 6), match='123'>
print(re.search("[0-9][0-9][0-9]", "foo456bar"))
# <re.Match object; span=(3, 6), match='456'>
print(re.search("[0-9][0-9][0-9]", "234baz"))
# <re.Match object; span=(0, 3), match='234'>
print(re.search("[0-9][0-9][0-9]", "qux678"))
# <re.Match object; span=(3, 6), match='678'>
print(re.search("[0-9][0-9][0-9]", "12foo34"))
# None

# The dot is a wildcard for any character except a newline
print(re.search("1.3", "foo123bar"))
# <re.Match object; span=(3, 6), match='123'>
print(re.search("1.3", "foo13bar"))
# None
