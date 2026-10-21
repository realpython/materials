"""Quantifiers: *, +, ?, {m}, {m,n}, and their non-greedy versions."""

import re

# * matches zero or more repetitions
print(re.search("foo-*bar", "foobar"))  # Zero dashes
# <re.Match object; span=(0, 6), match='foobar'>
print(re.search("foo-*bar", "foo-bar"))  # One dash
# <re.Match object; span=(0, 7), match='foo-bar'>
print(re.search("foo-*bar", "foo--bar"))  # Two dashes
# <re.Match object; span=(0, 8), match='foo--bar'>

print(re.search("foo.*bar", "# foo $qux@grault % bar #"))
# <re.Match object; span=(2, 23), match='foo $qux@grault % bar'>

# + matches one or more repetitions
print(re.search("foo-+bar", "foobar"))  # Zero dashes
# None
print(re.search("foo-+bar", "foo-bar"))  # One dash
# <re.Match object; span=(0, 7), match='foo-bar'>
print(re.search("foo-+bar", "foo--bar"))  # Two dashes
# <re.Match object; span=(0, 8), match='foo--bar'>

# ? matches zero or one repetition
print(re.search("foo-?bar", "foobar"))  # Zero dashes
# <re.Match object; span=(0, 6), match='foobar'>
print(re.search("foo-?bar", "foo-bar"))  # One dash
# <re.Match object; span=(0, 7), match='foo-bar'>
print(re.search("foo-?bar", "foo--bar"))  # Two dashes
# None

# Quantifying a character class
print(re.match("foo[1-9]*bar", "foobar"))
# <re.Match object; span=(0, 6), match='foobar'>
print(re.match("foo[1-9]*bar", "foo42bar"))
# <re.Match object; span=(0, 8), match='foo42bar'>
print(re.match("foo[1-9]+bar", "foobar"))
# None
print(re.match("foo[1-9]+bar", "foo42bar"))
# <re.Match object; span=(0, 8), match='foo42bar'>
print(re.match("foo[1-9]?bar", "foobar"))
# <re.Match object; span=(0, 6), match='foobar'>
print(re.match("foo[1-9]?bar", "foo42bar"))
# None

# Greedy vs non-greedy (lazy) quantifiers
print(re.search("<.*>", "%<foo> <bar> <baz>%"))
# <re.Match object; span=(1, 18), match='<foo> <bar> <baz>'>
print(re.search("<.*?>", "%<foo> <bar> <baz>%"))
# <re.Match object; span=(1, 6), match='<foo>'>
print(re.search("<.+>", "%<foo> <bar> <baz>%"))
# <re.Match object; span=(1, 18), match='<foo> <bar> <baz>'>
print(re.search("<.+?>", "%<foo> <bar> <baz>%"))
# <re.Match object; span=(1, 6), match='<foo>'>
print(re.search("ba?", "baaaa"))
# <re.Match object; span=(0, 2), match='ba'>
print(re.search("ba??", "baaaa"))
# <re.Match object; span=(0, 1), match='b'>

# {m} matches exactly m repetitions
print(re.search("x-{3}x", "x--x"))  # Two dashes
# None
print(re.search("x-{3}x", "x---x"))  # Three dashes
# <re.Match object; span=(0, 5), match='x---x'>
print(re.search("x-{3}x", "x----x"))  # Four dashes
# None

# {m,n} matches from m to n repetitions, inclusive
for i in range(1, 6):
    s = f"x{'-' * i}x"
    print(f"{i}  {s:10}", re.search("x-{2,4}x", s))
# 1  x-x        None
# 2  x--x       <re.Match object; span=(0, 4), match='x--x'>
# 3  x---x      <re.Match object; span=(0, 5), match='x---x'>
# 4  x----x     <re.Match object; span=(0, 6), match='x----x'>
# 5  x-----x    None

# Curly braces that don't hold a valid range match literally
print(re.search("x{}y", "x{}y"))
# <re.Match object; span=(0, 4), match='x{}y'>
print(re.search("x{foo}y", "x{foo}y"))
# <re.Match object; span=(0, 7), match='x{foo}y'>
print(re.search("x{a:b}y", "x{a:b}y"))
# <re.Match object; span=(0, 7), match='x{a:b}y'>
print(re.search("x{1,3,5}y", "x{1,3,5}y"))
# <re.Match object; span=(0, 9), match='x{1,3,5}y'>
print(re.search("x{foo,bar}y", "x{foo,bar}y"))
# <re.Match object; span=(0, 11), match='x{foo,bar}y'>

# {m,n}? is the non-greedy version of {m,n}
print(re.search("a{3,5}", "aaaaaaaa"))
# <re.Match object; span=(0, 5), match='aaaaa'>
print(re.search("a{3,5}?", "aaaaaaaa"))
# <re.Match object; span=(0, 3), match='aaa'>
