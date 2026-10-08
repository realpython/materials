"""Continuing a statement across lines with parentheses, brackets, or braces.

Code from the "Implicit Line Continuation" section of the tutorial, in the
order the tutorial presents it. Any statement with an open '(', '[', or '{'
is presumed incomplete until the matching closer is found, so it can run on
across as many lines as you like.

The blocks that only define a value are given a print() here so that
running the script shows you the result.
"""

# fmt: off
person1_age = 42
person2_age = 16
person3_age = 71

# The nested list from the previous section, made readable by the open
# brackets.
a = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(a)

# A long expression wrapped in grouping parentheses, as PEP 8 advocates.
someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65)
    or (person2_age >= 18 and person2_age <= 65)
    or (person3_age >= 18 and person3_age <= 65)
)
print(someone_is_of_working_age)

# Parentheses: expression grouping
x = (
    1 + 2
    + 3 + 4
    + 5 + 6
)
print(x)

# Parentheses: function call
print(
    'foo',
    'bar',
    'baz'
)

# Parentheses: method call
print(repr('abc'.center(
    9,
    '-'
)))

# Parentheses: tuple definition
t = (
    'a', 'b',
    'c', 'd'
)
print(t)

# Curly braces: dictionary definition
d = {
    'a': 1,
    'b': 2
}
print(d)

# Curly braces: set definition
x1 = {
    'foo',
    'bar',
    'baz'
}
# Deliberately not printed: the display order of a set of strings varies
# between runs, and the tutorial shows no output for this block either.

# Square brackets: list definition
a = [
    'foo', 'bar',
    'baz', 'qux'
]
print(a)

# Square brackets: indexing
print(repr(a[
 1
 ]))

# Square brackets: slicing
print(a[
 1:2
 ])

# Square brackets: dictionary key reference
print(d[
 'b'
 ])

# Implicit continuation stays in effect until every parenthesis, bracket,
# and brace has been closed. Indentation clarifies the nested structure.
a = [
    [
        ['foo', 'bar'],
        [1, 2, 3]
    ],
    {1, 3, 5},
    {
        'a': 1,
        'b': 2
    }
]
print(a)
# fmt: on
