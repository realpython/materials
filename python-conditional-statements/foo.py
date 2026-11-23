"""A block that is skipped because its condition is false.

The script file foo.py from the "Python: It's All About the Indentation"
section of the tutorial. The four indented print() calls form the block,
and only the last line runs.
"""

if "foo" in ["bar", "baz", "qux"]:
    print("Expression was true")
    print("Executing statement in suite")
    print("...")
    print("Done.")
print("After conditional")
