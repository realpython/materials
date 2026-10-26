"""Match object attributes: .pos, .endpos, .lastindex, .lastgroup, .re,
and .string.
"""

import re

# .pos and .endpos
re_obj = re.compile(r"\d+")
m = re_obj.search("foo123bar", 2, 7)
print(m)
# <re.Match object; span=(3, 6), match='123'>
print(m.pos, m.endpos)
# 2 7
m = re_obj.search("foo123bar")
print(m.pos, m.endpos)
# 0 9
m = re.search(r"\d+", "foo123bar")
print(m.pos, m.endpos)
# 0 9

# .lastindex
m = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(m.lastindex, m[m.lastindex])
# 3 baz
m = re.search(r"(\w+),(\w+),(\w+)?", "foo,bar,baz")
print(m.groups(), (m.lastindex, m[m.lastindex]))
# ('foo', 'bar', 'baz') (3, 'baz')
m = re.search(r"(\w+),(\w+),(\w+)?", "foo,bar,")
print(m.groups(), (m.lastindex, m[m.lastindex]))
# ('foo', 'bar', None) (2, 'bar')

# The outermost group is the last one to match
m = re.match("((a)(b))", "ab")
print(m.groups(), m.lastindex, m[m.lastindex])
# ('ab', 'a', 'b') 1 ab

# .lastgroup
s = "foo123bar456baz"
m = re.search(r"(?P<n1>\d+)\D*(?P<n2>\d+)", s)
print(m.lastgroup)
# n2
m = re.search(r"(\d+)\D*(\d+)", s)
print(m.groups(), m.lastgroup)
# ('123', '456') None
m = re.search(r"\d+\D*\d+", s)
print(m.groups(), m.lastgroup)
# () None

# .re is the (cached) compiled regular expression object
regex = r"(\w+),(\w+),(\w+)"
m1 = re.search(regex, "foo,bar,baz")
print(m1.re)
# re.compile('(\\w+),(\\w+),(\\w+)')
re_obj = re.compile(regex)
print(re_obj is m1.re)
# True
m2 = re_obj.search("qux,quux,corge")
print(m2)
# <re.Match object; span=(0, 14), match='qux,quux,corge'>
print(m2.re is re_obj is m1.re)
# True

print(m1.re.groups)
# 3
print(repr(m1.re.pattern))
# '(\\w+),(\\w+),(\\w+)'
print(m1.re.pattern == regex)
# True
print(m1.re.flags)
# 32
print(m1.re.match("quux,corge,grault"))
# <re.Match object; span=(0, 17), match='quux,corge,grault'>

# .string
m = re.search(r"(\w+),(\w+),(\w+)", "foo,bar,baz")
print(m.string)
# foo,bar,baz
re_obj = re.compile(r"(\w+),(\w+),(\w+)")
m = re_obj.search("foo,bar,baz")
print(m.string)
# foo,bar,baz
