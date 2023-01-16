try:
    x = int(input("x = "))
    y = int(input("y = "))
    z = x / y
except (ValueError, ZeroDivisionError) as ex:  # noqa: F841
    import bpython

    bpython.embed(locals(), banner="Post-Mortem Debugging:")
else:
    print(z)
