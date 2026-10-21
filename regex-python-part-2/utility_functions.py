"""Utility functions: re.split() and re.escape()."""

import re

# re.split() splits a string using a regex as the delimiter
print(re.split(r"\s*[,;/]\s*", "foo,bar  ;  baz / qux"))
# ['foo', 'bar', 'baz', 'qux']

# Capturing groups include the delimiters in the result
print(re.split(r"(\s*[,;/]\s*)", "foo,bar  ;  baz / qux"))
# ['foo', ',', 'bar', '  ;  ', 'baz', ' / ', 'qux']

# Process the tokens, then rejoin them with the original delimiters
string = "foo,bar  ;  baz / qux"
regex = r"(\s*[,;/]\s*)"
a = re.split(regex, string)
for i, s in enumerate(a):
    # This will be True for the tokens but not the delimiters
    if not re.fullmatch(regex, s):
        a[i] = f"<{s}>"
print("".join(a))
# <foo>,<bar>  ;  <baz> / <qux>

# Noncapturing groups leave the delimiters out
regex = r"(?:\s*[,;/]\s*)"
print(re.split(regex, string))
# ['foo', 'bar', 'baz', 'qux']

# Limit the number of splits with maxsplit
s = "foo, bar, baz, qux, quux, corge"
print(re.split(r",\s*", s))
# ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(re.split(r",\s*", s, maxsplit=3))
# ['foo', 'bar', 'baz', 'qux, quux, corge']

# Delimiters at the start or end produce empty strings
print(re.split("(/)", "/foo/bar/baz/"))
# ['', '/', 'foo', '/', 'bar', '/', 'baz', '/', '']

# re.escape() backslash-escapes characters with special meaning
print(re.match("foo^bar(baz)|qux", "foo^bar(baz)|qux"))
# None
print(re.match(r"foo\^bar\(baz\)\|qux", "foo^bar(baz)|qux"))
# <re.Match object; span=(0, 16), match='foo^bar(baz)|qux'>
print(re.escape("foo^bar(baz)|qux") == r"foo\^bar\(baz\)\|qux")
# True
print(re.match(re.escape("foo^bar(baz)|qux"), "foo^bar(baz)|qux"))
# <re.Match object; span=(0, 16), match='foo^bar(baz)|qux'>
