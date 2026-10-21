"""Modifying regex matching with flags, combining flags, and setting or
clearing flags within a regex.
"""

import re

# re.I / re.IGNORECASE
print(re.search("a+", "aaaAAA"))
# <re.Match object; span=(0, 3), match='aaa'>
print(re.search("A+", "aaaAAA"))
# <re.Match object; span=(3, 6), match='AAA'>
print(re.search("a+", "aaaAAA", re.I))
# <re.Match object; span=(0, 6), match='aaaAAA'>
print(re.search("A+", "aaaAAA", re.IGNORECASE))
# <re.Match object; span=(0, 6), match='aaaAAA'>
print(re.search("[a-z]+", "aBcDeF"))
# <re.Match object; span=(0, 1), match='a'>
print(re.search("[a-z]+", "aBcDeF", re.I))
# <re.Match object; span=(0, 6), match='aBcDeF'>

# re.M / re.MULTILINE
s = "foo\nbar\nbaz"
print(re.search("^bar", s))
# None
print(re.search("baz$", s))
# <re.Match object; span=(8, 11), match='baz'>
print(re.search("^bar", s, re.MULTILINE))
# <re.Match object; span=(4, 7), match='bar'>
print(re.search("bar$", s, re.M))
# <re.Match object; span=(4, 7), match='bar'>

# MULTILINE doesn't affect \A and \Z
print(re.search(r"\Abar", s, re.MULTILINE))
# None
print(re.search(r"bar\Z", s, re.MULTILINE))
# None

# re.S / re.DOTALL
print(re.search("foo.bar", "foo\nbar"))
# None
print(re.search("foo.bar", "foo\nbar", re.DOTALL))
# <re.Match object; span=(0, 7), match='foo\nbar'>
print(re.search("foo.bar", "foo\nbar", re.S))
# <re.Match object; span=(0, 7), match='foo\nbar'>

# re.X / re.VERBOSE
regex = r"^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$"
print(re.search(regex, "(712) 414-9229"))
# <re.Match object; span=(0, 14), match='(712) 414-9229'>

regex = r"""^               # Start of string
            (\(\d{3}\))?    # Optional area code
            \s*             # Optional whitespace
            \d{3}           # Three-digit prefix
            [-.]            # Separator character
            \d{4}           # Four-digit line number
            $               # Anchor at end of string
            """
print(re.search(regex, "414.9229", re.VERBOSE))
# <re.Match object; span=(0, 8), match='414.9229'>
print(re.search(regex, "414-9229", re.VERBOSE))
# <re.Match object; span=(0, 8), match='414-9229'>
print(re.search(regex, "(712)414-9229", re.X))
# <re.Match object; span=(0, 13), match='(712)414-9229'>
print(re.search(regex, "(712) 414-9229", re.X))
# <re.Match object; span=(0, 14), match='(712) 414-9229'>

# In VERBOSE mode, escape significant spaces or put them in a class
print(re.search("foo bar", "foo bar", re.VERBOSE))
# None
print(re.search(r"foo\ bar", "foo bar", re.VERBOSE))
# <re.Match object; span=(0, 7), match='foo bar'>
print(re.search("foo[ ]bar", "foo bar", re.VERBOSE))
# <re.Match object; span=(0, 7), match='foo bar'>

# re.A / re.ASCII and re.U / re.UNICODE
s = "\u0967\u096a\u096c"
print(s)
# १४६
print(re.search(r"\d+", s))
# <re.Match object; span=(0, 3), match='१४६'>

s = "sch\u00f6n"
print(s)
# schön
print(re.search(r"\w+", s, re.ASCII))
# <re.Match object; span=(0, 3), match='sch'>
print(re.search(r"\w+", s, re.UNICODE))
# <re.Match object; span=(0, 5), match='schön'>
print(re.search(r"\w+", s))
# <re.Match object; span=(0, 5), match='schön'>

# Combining flags with bitwise OR
print(re.search("^bar", "FOO\nBAR\nBAZ", re.I | re.M))
# <re.Match object; span=(4, 7), match='BAR'>

# Setting flags within the regex: (?<flags>)
print(re.search("(?im)^bar", "FOO\nBAR\nBAZ\n"))
# <re.Match object; span=(4, 7), match='BAR'>
print(re.search("(?s)foo.bar.baz", "foo\nbar\nbaz"))
# <re.Match object; span=(0, 11), match='foo\nbar\nbaz'>

# Global flags must come first (an error since Python 3.11)
try:
    re.search("foo.bar.baz(?s)", "foo\nbar\nbaz")
except re.error as e:
    print(f"{type(e).__name__}: {e}")
# PatternError: global flags not at the start of the expression at position 11
# (On Python 3.12 and earlier, the exception class is named error.)

# Setting or clearing flags for a group: (?<set_flags>-<remove_flags>:...)
print(re.search("(?i:foo)bar", "FOObar"))
# <re.Match object; span=(0, 6), match='FOObar'>
print(re.search("(?i:foo)bar", "FOOBAR"))
# None
print(re.search("(?-i:foo)bar", "FOOBAR", re.IGNORECASE))
# None

# Overriding the encoding for a group (requires Python 3.7 or later)
print(re.search(r"(?a:\w+)", s))
# <re.Match object; span=(0, 3), match='sch'>
print(re.search(r"(?u:\w+)", s))
# <re.Match object; span=(0, 5), match='schön'>

# You can set an encoding this way, but you can't remove it
try:
    re.search(r"(?-a:\w+)", s)
except re.error as e:
    print(f"{type(e).__name__}: {e}")
# PatternError: bad inline flags: cannot turn off flags 'a', 'u' and 'L' at position 4
# (On Python 3.12 and earlier, the exception class is named error.)
