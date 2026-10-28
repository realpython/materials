"""Metacharacters that match a single character: [], ., \\w, \\W, \\d, \\D,
\\s, and \\S.
"""

import re

# Character classes: []
print(re.search("ba[artz]", "foobarqux"))
# <re.Match object; span=(3, 6), match='bar'>
print(re.search("ba[artz]", "foobazqux"))
# <re.Match object; span=(3, 6), match='baz'>

print(re.search("[a-z]", "FOObar"))
# <re.Match object; span=(3, 4), match='b'>
print(re.search("[0-9][0-9]", "foo123bar"))
# <re.Match object; span=(3, 5), match='12'>
print(re.search("[0-9a-fA-F]", "--- a0 ---"))
# <re.Match object; span=(4, 5), match='a'>

# A leading ^ complements the class
print(re.search("[^0-9]", "12345foo"))
# <re.Match object; span=(5, 6), match='f'>

# Anywhere else, ^ is a literal character
print(re.search("[#:^]", "foo^bar:baz#qux"))
# <re.Match object; span=(3, 4), match='^'>

# A literal hyphen goes first, last, or escaped
print(re.search("[-abc]", "123-456"))
# <re.Match object; span=(3, 4), match='-'>
print(re.search("[abc-]", "123-456"))
# <re.Match object; span=(3, 4), match='-'>
print(re.search(r"[ab\-c]", "123-456"))
# <re.Match object; span=(3, 4), match='-'>

# A literal ] goes first or escaped
print(re.search("[]]", "foo[1]"))
# <re.Match object; span=(5, 6), match=']'>
print(re.search(r"[ab\]cd]", "foo[1]"))
# <re.Match object; span=(5, 6), match=']'>

# Other metacharacters are literal inside a class
print(re.search("[)*+|]", "123*456"))
# <re.Match object; span=(3, 4), match='*'>
print(re.search("[)*+|]", "123+456"))
# <re.Match object; span=(3, 4), match='+'>

# The dot wildcard: any character except a newline
print(re.search("foo.bar", "fooxbar"))
# <re.Match object; span=(0, 7), match='fooxbar'>
print(re.search("foo.bar", "foobar"))
# None
print(re.search("foo.bar", "foo\nbar"))
# None

# \w and \W: word and non-word characters
print(re.search(r"\w", "#(.a$@&"))
# <re.Match object; span=(3, 4), match='a'>
print(re.search("[a-zA-Z0-9_]", "#(.a$@&"))
# <re.Match object; span=(3, 4), match='a'>
print(re.search(r"\W", "a_1*3Qb"))
# <re.Match object; span=(3, 4), match='*'>
print(re.search("[^a-zA-Z0-9_]", "a_1*3Qb"))
# <re.Match object; span=(3, 4), match='*'>

# \d and \D: decimal digits and non-digits
print(re.search(r"\d", "abc4def"))
# <re.Match object; span=(3, 4), match='4'>
print(re.search(r"\D", "234Q678"))
# <re.Match object; span=(3, 4), match='Q'>

# \s and \S: whitespace and non-whitespace (newlines count as whitespace)
print(re.search(r"\s", "foo\nbar baz"))
# <re.Match object; span=(3, 4), match='\n'>
print(re.search(r"\S", "  \n foo  \n  "))
# <re.Match object; span=(4, 5), match='f'>

# Special classes also work inside square brackets
print(re.search(r"[\d\w\s]", "---3---"))
# <re.Match object; span=(3, 4), match='3'>
print(re.search(r"[\d\w\s]", "---a---"))
# <re.Match object; span=(3, 4), match='a'>
print(re.search(r"[\d\w\s]", "--- ---"))
# <re.Match object; span=(3, 4), match=' '>
