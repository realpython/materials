"""Displaying how the regex parser interprets a pattern with re.DEBUG.

Python 3.8 and later print the parse tree shown below, then a blank line
and a dump of the compiled pattern's internal opcodes. This script prints
only the parse tree, which is the part the tutorial discusses.
"""

import contextlib
import io
import re


def show_parse_tree(regex, string, flags=re.DEBUG):
    """Search string with a DEBUG flag and print only the parse tree."""
    re.purge()  # Clear the cache so the pattern compiles and prints again
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        match = re.search(regex, string, flags)
    print(buffer.getvalue().split("\n\n")[0])
    print(match)


show_parse_tree("foo.bar", "fooxbar")
# LITERAL 102
# LITERAL 111
# LITERAL 111
# ANY None
# LITERAL 98
# LITERAL 97
# LITERAL 114
# <re.Match object; span=(0, 7), match='fooxbar'>

show_parse_tree(r"^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$", "414.9229")
# AT AT_BEGINNING
# MAX_REPEAT 0 1
#   SUBPATTERN 1 0 0
#     LITERAL 40
#     MAX_REPEAT 3 3
#       IN
#         CATEGORY CATEGORY_DIGIT
#     LITERAL 41
# MAX_REPEAT 0 MAXREPEAT
#   IN
#     CATEGORY CATEGORY_SPACE
# MAX_REPEAT 3 3
#   IN
#     CATEGORY CATEGORY_DIGIT
# IN
#   LITERAL 45
#   LITERAL 46
# MAX_REPEAT 4 4
#   IN
#     CATEGORY CATEGORY_DIGIT
# AT AT_END
# <re.Match object; span=(0, 8), match='414.9229'>

# {2,4} is a quantifier, so the tree contains MAX_REPEAT
show_parse_tree("x[123]{2,4}y", "x222y")
# LITERAL 120
# MAX_REPEAT 2 4
#   IN
#     LITERAL 49
#     LITERAL 50
#     LITERAL 51
# LITERAL 121
# <re.Match object; span=(0, 5), match='x222y'>

# {foo} isn't a valid quantifier, so it's matched literally
show_parse_tree("x[123]{foo}y", "x222y")
# LITERAL 120
# IN
#   LITERAL 49
#   LITERAL 50
#   LITERAL 51
# LITERAL 123
# LITERAL 102
# LITERAL 111
# LITERAL 111
# LITERAL 125
# LITERAL 121
# None

# The re module has no single-letter DEBUG flag, but you can define one
print(hasattr(re, "D"))
# False
re.D = re.DEBUG
show_parse_tree("foo", "foo", re.D)
# LITERAL 102
# LITERAL 111
# LITERAL 111
# <re.Match object; span=(0, 3), match='foo'>
