"""Where whitespace matters to the interpreter, and where it matters to you.

Code from the "Whitespace" section of the tutorial. Whitespace is mostly
optional between tokens, but leaving it out hurts readability, and it
becomes mandatory when it is the only thing separating an identifier from
a keyword.

The cramped examples below are copied from the tutorial verbatim. They are
not code you should write.

Three error examples from the tutorial are not reproduced here because they
cannot run: 'sin [...]' raises a NameError, and 'y is20' and "'qux' notin
[...]" both raise a SyntaxError.
"""

# fmt: off
# No whitespace at all -- the interpreter handles all of these fine.
x=3;y=12  # noqa: E702
print(x+y)

print((x==3)and(x<y))

a=['foo','bar','baz']
print(a)

d={'foo':3,'bar':4}
print(d)

x,y,z='foo',14,21.1
print((x,y,z))

z='foo'"bar"'baz'#Comment
print(repr(z))

# Compare these two fragments. Most people find the second easier to read.
value1=100
value2=200
v=(value1>=0)and(value1<value2)
print(v)

value1 = 100
value2 = 200
v = (value1 >= 0) and (value1 < value2)
print(v)

# String literals can be juxtaposed with or without whitespace. The effect
# is concatenation, exactly as though you had used the + operator.
s = "foo"'bar''''baz'''
print(repr(s))

s = 'foo' "bar" '''baz'''
print(repr(s))

# Whitespace is required here to separate the identifier s from the
# keyword in, and to separate the keywords not and in.
s = 'bar'

print(s in ['foo', 'bar', 'baz'])

print('qux' not in ['foo', 'bar', 'baz'])
# fmt: on
