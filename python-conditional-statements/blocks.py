"""Nested blocks, where each indent opens a block and each outdent ends one.

The script file blocks.py from the "Python: It's All About the Indentation"
section of the tutorial.
"""

# fmt: off
# Does line execute?                        Yes    No
#                                           ---    --
if "foo" in ["foo", "bar", "baz"]:        #  x
    print("Outer condition is true")      #  x

    if 10 > 20:                           #  x
        print("Inner condition 1")        #        x

    print("Between inner conditions")     #  x

    if 10 < 20:                           #  x
        print("Inner condition 2")        #  x

    print("End of outer condition")       #  x
print("After outer condition")            #  x
# fmt: on
