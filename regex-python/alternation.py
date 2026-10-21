"""Miscellaneous metacharacters: inline comments with (?#...) and
alternation with |.
"""

import re

# The parser ignores (?#...) comments
print(re.search("bar(?#This is a comment) *baz", "foo bar baz qux"))
# <re.Match object; span=(4, 11), match='bar baz'>

# Alternation matches one of several regexes
print(re.search("foo|bar|baz", "bar"))
# <re.Match object; span=(0, 3), match='bar'>
print(re.search("foo|bar|baz", "baz"))
# <re.Match object; span=(0, 3), match='baz'>
print(re.search("foo|bar|baz", "quux"))
# None

# Alternation returns the first alternative that matches, not the longest
print(re.search("foo", "foograult"))
# <re.Match object; span=(0, 3), match='foo'>
print(re.search("grault", "foograult"))
# <re.Match object; span=(3, 9), match='grault'>
print(re.search("foo|grault", "foograult"))
# <re.Match object; span=(0, 3), match='foo'>

# Combining alternation with grouping and quantifiers
print(re.search("(foo|bar|baz)+", "foofoofoo"))
# <re.Match object; span=(0, 9), match='foofoofoo'>
print(re.search("(foo|bar|baz)+", "bazbazbazbaz"))
# <re.Match object; span=(0, 12), match='bazbazbazbaz'>
print(re.search("(foo|bar|baz)+", "barbazfoo"))
# <re.Match object; span=(0, 9), match='barbazfoo'>
print(re.search("([0-9]+|[a-f]+)", "456"))
# <re.Match object; span=(0, 3), match='456'>
print(re.search("([0-9]+|[a-f]+)", "ffda"))
# <re.Match object; span=(0, 4), match='ffda'>
