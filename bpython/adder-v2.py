try:
    x = int(input("x = "))
    y = int(input("y = "))
    import bpdb; bpdb.set_trace()
    z = x / y
except (ValueError, ZeroDivisionError) as ex:
    import bpython
    bpython.embed(locals(), banner="Post-Mortem Debugging:")
else:
    print(z)
