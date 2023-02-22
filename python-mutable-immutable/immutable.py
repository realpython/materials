class Immutable:
    def __init__(self, magnitude):
        super().__setattr__("magnitude", magnitude)

    def __setattr__(self, name, value):
        raise AttributeError(f"can't set attribute '{name}'")

    def __delattr__(self, name):
        raise AttributeError(f"can't delete attribute '{name}'")
