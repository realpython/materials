class NonDeletable:
    def __init__(self, value):
        self.value = value

    def __delattr__(self, name):
        raise AttributeError(
            f"{type(self).__name__} object doesn't support attribute deletion"
        )
