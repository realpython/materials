"""Writing an if statement, or each of its clauses, on a single line.

Code from the "One-Line if Statements" section of the tutorial. The one-line
layout is the point of this section, so the formatter is switched off and
the style warnings are silenced. PEP 8 recommends against writing code
like this.
"""

# fmt: off
# The statements after the colon form one suite: all of them run, or none.
if "f" in "foo": print("1"); print("2"); print("3")  # noqa: E701, E702
if "z" in "foo": print("1"); print("2"); print("3")  # noqa: E701, E702

for x in (2, 3):
    if x == 1: print("foo"); print("bar"); print("baz")  # noqa: E701, E702
    elif x == 2: print("qux"); print("quux")  # noqa: E701, E702
    else: print("corge"); print("grault")  # noqa: E701, E702
# fmt: on

# Most people find the multi-line form easier to read.
x = 3
if x == 1:
    print("foo")
    print("bar")
    print("baz")
elif x == 2:
    print("qux")
    print("quux")
else:
    print("corge")
    print("grault")


# A simple one-line if is usually acceptable.
def foo():
    print("Calling foo()")


debugging = True  # Set to True to turn debugging on.

# fmt: off
if debugging: print("About to call function foo()")  # noqa: E701
# fmt: on
foo()
