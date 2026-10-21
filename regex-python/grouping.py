"""Grouping constructs, capturing groups, backreferences, named groups,
non-capturing groups, and conditional matches.
"""

import re

# A group matches its contents, just like the bare regex
print(re.search("(bar)", "foo bar baz"))
# <re.Match object; span=(4, 7), match='bar'>
print(re.search("bar", "foo bar baz"))
# <re.Match object; span=(4, 7), match='bar'>

# A quantifier after a group applies to the whole group
print(re.search("(bar)+", "foo bar baz"))
# <re.Match object; span=(4, 7), match='bar'>
print(re.search("(bar)+", "foo barbar baz"))
# <re.Match object; span=(4, 10), match='barbar'>
print(re.search("(bar)+", "foo barbarbarbar baz"))
# <re.Match object; span=(4, 16), match='barbarbarbar'>

print(re.search("(ba[rz]){2,4}(qux)?", "bazbarbazqux"))
# <re.Match object; span=(0, 12), match='bazbarbazqux'>
print(re.search("(ba[rz]){2,4}(qux)?", "barbar"))
# <re.Match object; span=(0, 6), match='barbar'>

# Groups can be nested
print(re.search(r"(foo(bar)?)+(\d\d\d)?", "foofoobar"))
# <re.Match object; span=(0, 9), match='foofoobar'>
print(re.search(r"(foo(bar)?)+(\d\d\d)?", "foofoobar123"))
# <re.Match object; span=(0, 12), match='foofoobar123'>
print(re.search(r"(foo(bar)?)+(\d\d\d)?", "foofoo123"))
# <re.Match object; span=(0, 9), match='foofoo123'>

# Capturing groups: .groups() and .group()
m = re.search(r"(\w+),(\w+),(\w+)", "foo,quux,baz")
print(m)
# <re.Match object; span=(0, 12), match='foo,quux,baz'>
print(m.groups())
# ('foo', 'quux', 'baz')
print(m.group(1), m.group(2), m.group(3))
# foo quux baz
print(m.group(0))
# foo,quux,baz
print(m.group())
# foo,quux,baz
print(m.group(2, 3))
# ('quux', 'baz')
print(m.group(3, 2, 1))
# ('baz', 'quux', 'foo')
print((m.group(3), m.group(2), m.group(1)))
# ('baz', 'quux', 'foo')

# Numbered backreferences
regex = r"(\w+),\1"
m = re.search(regex, "foo,foo")
print(m, m.group(1))
# <re.Match object; span=(0, 7), match='foo,foo'> foo
m = re.search(regex, "qux,qux")
print(m, m.group(1))
# <re.Match object; span=(0, 7), match='qux,qux'> qux
print(re.search(regex, "foo,qux"))
# None

# Without a raw string, Python reads "\1" as the character with octal value 1
print(re.search("([a-z])#\1", "d#d"))
# None
print(oct(ord("\1")))
# 0o1
print(re.search(r"([a-z])#\1", "d#d"))
# <re.Match object; span=(0, 3), match='d#d'>

# Named groups: (?P<name><regex>)
m = re.search(r"(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)", "foo,quux,baz")
print(m.groups())
# ('foo', 'quux', 'baz')
print(m.group("w1"), m.group(1))
# foo foo
print(m.group("w3"))
# baz
print(m.group("w1", "w2", "w3"))
# ('foo', 'quux', 'baz')
print(m.group(1, 2, 3))
# ('foo', 'quux', 'baz')

# Named backreferences: (?P=name)
m = re.search(r"(?P<word>\w+),(?P=word)", "foo,foo")
print(m, m.group("word"))
# <re.Match object; span=(0, 7), match='foo,foo'> foo
m = re.match(r"(?P<num>\d+)\.(?P=num)", "135.135")
print(m, m.group("num"))
# <re.Match object; span=(0, 7), match='135.135'> 135

# Non-capturing groups: (?:<regex>)
m = re.search(r"(\w+),(?:\w+),(\w+)", "foo,quux,baz")
print(m.groups())
# ('foo', 'baz')
print(m.group(1), m.group(2))
# foo baz

# Conditional match on a numbered group
regex = r"^(###)?foo(?(1)bar|baz)"
print(re.search(regex, "###foobar"))
# <re.Match object; span=(0, 9), match='###foobar'>
print(re.search(regex, "###foobaz"))
# None
print(re.search(regex, "foobar"))
# None
print(re.search(regex, "foobaz"))
# <re.Match object; span=(0, 6), match='foobaz'>

# Conditional match on a named group
regex = r"^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$"
print(re.search(regex, "foo"))
# <re.Match object; span=(0, 3), match='foo'>
print(re.search(regex, "#foo#"))
# <re.Match object; span=(0, 5), match='#foo#'>
print(re.search(regex, "@foo@"))
# <re.Match object; span=(0, 5), match='@foo@'>
print(re.search(regex, "#foo"))
# None
print(re.search(regex, "foo@"))
# None
print(re.search(regex, "#foo@"))
# None
print(re.search(regex, "@foo#"))
# None
