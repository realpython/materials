"""Lookahead and lookbehind assertions."""

import re

# Positive lookahead: (?=<lookahead_regex>)
print(re.search("foo(?=[a-z])", "foobar"))
# <re.Match object; span=(0, 3), match='foo'>
print(re.search("foo(?=[a-z])", "foo123"))
# None

# Compare with a group, which consumes the character
print(re.search("foo([a-z])", "foobar"))
# <re.Match object; span=(0, 4), match='foob'>

# A lookahead doesn't advance the parser past what it matches
m = re.search("foo(?=[a-z])(?P<ch>.)", "foobar")
print(m.group("ch"))
# b
m = re.search("foo([a-z])(?P<ch>.)", "foobar")
print(m.group("ch"))
# a

# Negative lookahead: (?!<lookahead_regex>)
print(re.search("foo(?![a-z])", "foobar"))
# None
print(re.search("foo(?![a-z])", "foo123"))
# <re.Match object; span=(0, 3), match='foo'>

# Positive lookbehind: (?<=<lookbehind_regex>)
print(re.search("(?<=foo)bar", "foobar"))
# <re.Match object; span=(3, 6), match='bar'>
print(re.search("(?<=qux)bar", "foobar"))
# None

# A lookbehind must match a fixed-width pattern
try:
    re.search("(?<=a+)def", "aaadef")
except re.error as e:
    print(f"{type(e).__name__}: {e}")
# PatternError: look-behind requires fixed-width pattern
# (On Python 3.12 and earlier, the exception class is named error.)
print(re.search("(?<=a{3})def", "aaadef"))
# <re.Match object; span=(3, 6), match='def'>

# Negative lookbehind: (?<!<lookbehind_regex>)
print(re.search("(?<!foo)bar", "foobar"))
# None
print(re.search("(?<!qux)bar", "foobar"))
# <re.Match object; span=(3, 6), match='bar'>
