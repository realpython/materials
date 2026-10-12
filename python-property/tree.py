class TreeNode:
    def __init__(self, data):
        self._data = data
        self._children = []

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = value
        else:
            del self.children
            self._children.append(value)

    @children.deleter
    def children(self):
        self._children.clear()

    def __repr__(self):
        return f'{self.__class__.__name__}("{self._data}")'
