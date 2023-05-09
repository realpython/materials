class PowerFactory:
    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, base):
        return base**self.exponent
