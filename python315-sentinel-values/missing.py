class _MissingType:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return self._name

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        return self

    def __reduce__(self):
        return self._name

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return id(self)
