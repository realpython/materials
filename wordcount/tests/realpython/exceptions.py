class RealPythonAssertionError(AssertionError):
    def __init__(self, expected, actual, message=None):
        self.expected = expected
        self.actual = actual
        self.message = message
