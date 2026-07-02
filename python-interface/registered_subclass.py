from virtual_subclass import Double

print(issubclass(float, Double))
print(isinstance(1.2345, Double))


@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""


print(issubclass(Double64, Double))
