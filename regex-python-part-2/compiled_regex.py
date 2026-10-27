"""Compiled regular expression objects: re.compile(), its methods, and
its attributes.
"""

import re

# The three equivalent ways to search with a regex
re_obj = re.compile(r"(\d+)")
print(re.search(r"(\d+)", "foo123bar"))
# <re.Match object; span=(3, 6), match='123'>
print(re.search(re_obj, "foo123bar"))
# <re.Match object; span=(3, 6), match='123'>
print(re_obj.search("foo123bar"))
# <re.Match object; span=(3, 6), match='123'>

# Flags passed to re.compile() apply to every search
r1 = re.search("ba[rz]", "FOOBARBAZ", flags=re.I)
re_obj = re.compile("ba[rz]", flags=re.I)
r2 = re.search(re_obj, "FOOBARBAZ")
r3 = re_obj.search("FOOBARBAZ")
print(r1)
# <re.Match object; span=(3, 6), match='BAR'>
print(r2)
# <re.Match object; span=(3, 6), match='BAR'>
print(r3)
# <re.Match object; span=(3, 6), match='BAR'>

# Compiling separates the regex definition from its uses
s1, s2, s3, s4 = "foo.bar", "foo123bar", "baz99", "qux & grault"
re_obj = re.compile(r"\d+")
print(re_obj.search(s1))
# None
print(re_obj.search(s2))
# <re.Match object; span=(3, 6), match='123'>
print(re_obj.search(s3))
# <re.Match object; span=(3, 5), match='99'>
print(re_obj.search(s4))
# None

# The pos and endpos arguments restrict the search to a slice
re_obj = re.compile(r"\d+")
s = "foo123barbaz"
print(re_obj.search(s))
# <re.Match object; span=(3, 6), match='123'>
print(s[6:9])
# bar
print(re_obj.search(s, 6, 9))
# None

# Anchors still refer to the whole string, not the slice
re_obj = re.compile("^bar")
s = "foobarbaz"
print(s[3:])
# barbaz
print(re_obj.search(s, 3))
# None

# Regular expression object attributes
re_obj = re.compile(r"(?m)(\w+),(\w+)", re.I)
print(re_obj.flags)
# 42
print(repr(re.I | re.M | re.UNICODE))
# re.IGNORECASE|re.UNICODE|re.MULTILINE
print(re_obj.groups)
# 2
print(repr(re_obj.pattern))
# '(?m)(\\w+),(\\w+)'

re_obj = re.compile(r"(?P<w1>),(?P<w2>)")
print(repr(re_obj.groupindex))
# mappingproxy({'w1': 1, 'w2': 2})
print(re_obj.groupindex["w1"])
# 1
print(re_obj.groupindex["w2"])
# 2
