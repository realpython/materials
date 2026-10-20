"""Match object methods: .group(), .__getitem__(), .groups(),
.groupdict(), .expand(), .start(), .end(), and .span().
"""

import re

# A match object is truthy
m = re.search("bar", "foo.bar.baz")
print(m)
# <re.Match object; span=(4, 7), match='bar'>
print(bool(m))
# True
if re.search("bar", "foo.bar.baz"):
    print("Found a match")
# Found a match

# .group() with numbered and named groups
m = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(m.group(1), m.group(3))
# foo baz
print(m.group(1, 3))
# ('foo', 'baz')
print(m.group(3, 3, 1, 1, 2, 2))
# ('baz', 'baz', 'foo', 'foo', 'bar', 'bar')
print(m.group(0))
# foo,bar,baz
print(m.group())
# foo,bar,baz
try:
    m.group(4)
except IndexError as e:
    print(f"IndexError: {e}")
# IndexError: no such group

m = re.match(r"(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)", "quux,corge,grault")
print(m.group("w1"), m.group("w3"))
# quux grault
print(m.group("w3", "w1", "w1", "w2"))
# ('grault', 'quux', 'quux', 'corge')

# A nonparticipating group returns None
m = re.search(r"(\w+),(\w+),(\w+)?", "foo,bar,")
print(m)
# <re.Match object; span=(0, 8), match='foo,bar,'>
print(m.group(1, 2))
# ('foo', 'bar')
print(m.group(3))
# None

# A repeated group keeps only its last match
m = re.match(r"(\w{3},)+", "foo,bar,baz,qux")
print(m)
# <re.Match object; span=(0, 12), match='foo,bar,baz,'>
print(m.group(1))
# baz,

# match[n] is syntactic sugar for match.__getitem__(n) and match.group(n)
m = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(m.group(2), m.__getitem__(2), m[2])
# bar bar bar
m = re.match(
    r"foo,(?P<w1>\w+),(?P<w2>\w+),qux",
    "foo,bar,baz,qux",
)
print(m.group("w2"), m["w2"])
# baz baz

# .groups() and .groupdict(), with and without a default
m = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(m.groups())
# ('foo', 'bar', 'baz')
m = re.search(r"(\w+),(\w+),(\w+)?", "foo,bar,")
print(m.groups())
# ('foo', 'bar', None)
print(m.groups(default="---"))
# ('foo', 'bar', '---')

m = re.match(
    r"foo,(?P<w1>\w+),(?P<w2>\w+),qux",
    "foo,bar,baz,qux",
)
print(m.groupdict())
# {'w1': 'bar', 'w2': 'baz'}
print(m.groupdict()["w2"])
# baz
m = re.match(
    r"foo,(?P<w1>\w+),(?P<w2>\w+)?,qux",
    "foo,bar,,qux",
)
print(m.groupdict())
# {'w1': 'bar', 'w2': None}
print(m.groupdict(default="---"))
# {'w1': 'bar', 'w2': '---'}

# .expand() performs backreference substitution on a template
m = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(m.expand(r"\2"))
# bar
print(m.expand(r"[\3] -> [\1]"))
# [baz] -> [foo]
m = re.search(r"(?P<num>\d+)", "foo123qux")
print(m.expand(r"--- \g<num> ---"))
# --- 123 ---

# .start(), .end(), and .span()
s = "foo123bar456baz"
m = re.search(r"\d+", s)
print(m.start(), m.end())
# 3 6
print(s[m.start() : m.end()])
# 123

m = re.search(r"(\d+)\D*(?P<num>\d+)", s)
print(m)
# <re.Match object; span=(3, 12), match='123bar456'>
print(m.start(1), m.end(1), s[m.start(1) : m.end(1)])
# 3 6 123
print(m.start("num"), m.end("num"), s[m.start("num") : m.end("num")])
# 9 12 456
print(m.span(), m.span(1), m.span("num"))
# (3, 12) (3, 6) (9, 12)

# A group matching an empty string, and a nonparticipating group
m = re.search(r"foo(\d*)bar", "foobar")
print(repr(m[1]), (m.start(1), m.end(1)))
# '' (3, 3)
m = re.search(r"(\w+),(\w+),(\w+)?", "foo,bar,")
print(m.start(3), m.end(3))
# -1 -1
