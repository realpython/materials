def f(arg):
    print(f"-> f({arg}) = {arg}")
    return arg


print(f(0))
print(f(False))
print(f(1.5))

# Short-circuit evaluation in a compound or expression
print(f(0) or f(False) or f(1) or f(2) or f(3))

# Short-circuit evaluation in a compound and expression
print(f(1) and f(False) and f(2) and f(3))
print(f(1) and f(0.0) and f(2) and f(3))

# When every operand is truthy, and returns the rightmost one
print(f(1) and f(2.2) and f("Hello"))
print(f(1) and f(2.2) and f(0))
