class Immutable:
    def __init__(self, value):
        super().__setattr__("value", value)

    def __setattr__(self, name, attr_value):
        raise AttributeError(f"can't set attribute '{name}'")

    def __delattr__(self, name):
        raise AttributeError(f"can't delete attribute '{name}'")
