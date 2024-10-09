class PowerFactory:
    """Create instances that can calculate powers."""

    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, number):
        return number**self.exponent


cubed = PowerFactory(3)
print(cubed(13))
