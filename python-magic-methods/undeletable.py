class NonDeletable:
    class_attribute = 1

    def __init__(self, value):
        self.value = value

    def __delattr__(self, name):
        raise AttributeError(
            f"{type(self).__name__} doesn't support attribute deletion"
        )
