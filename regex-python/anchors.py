"""Anchors: ^, \\A, $, \\Z, \\b, and \\B."""

import re

# ^ and \A anchor a match to the start of the string
print(re.search("^foo", "foobar"))
# <re.Match object; span=(0, 3), match='foo'>
print(re.search("^foo", "barfoo"))
# None
print(re.search(r"\Afoo", "foobar"))
# <re.Match object; span=(0, 3), match='foo'>
print(re.search(r"\Afoo", "barfoo"))
# None

# $ and \Z anchor a match to the end of the string
print(re.search("bar$", "foobar"))
# <re.Match object; span=(3, 6), match='bar'>
print(re.search("bar$", "barfoo"))
# None
print(re.search(r"bar\Z", "foobar"))
# <re.Match object; span=(3, 6), match='bar'>
print(re.search(r"bar\Z", "barfoo"))
# None

# $ (but not \Z) also matches before a single trailing newline
print(re.search("bar$", "foobar\n"))
# <re.Match object; span=(3, 6), match='bar'>

# \b anchors a match to a word boundary
print(re.search(r"\bbar", "foo bar"))
# <re.Match object; span=(4, 7), match='bar'>
print(re.search(r"\bbar", "foo.bar"))
# <re.Match object; span=(4, 7), match='bar'>
print(re.search(r"\bbar", "foobar"))
# None
print(re.search(r"foo\b", "foo bar"))
# <re.Match object; span=(0, 3), match='foo'>
print(re.search(r"foo\b", "foo.bar"))
# <re.Match object; span=(0, 3), match='foo'>
print(re.search(r"foo\b", "foobar"))
# None

# \b on both ends matches a whole word
print(re.search(r"\bbar\b", "foo bar baz"))
# <re.Match object; span=(4, 7), match='bar'>
print(re.search(r"\bbar\b", "foo(bar)baz"))
# <re.Match object; span=(4, 7), match='bar'>
print(re.search(r"\bbar\b", "foobarbaz"))
# None

# \B anchors a match to a location that isn't a word boundary
print(re.search(r"\Bfoo\B", "foo"))
# None
print(re.search(r"\Bfoo\B", ".foo."))
# None
print(re.search(r"\Bfoo\B", "barfoobaz"))
# <re.Match object; span=(3, 6), match='foo'>
