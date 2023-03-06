class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value).upper()

    @name.deleter
    def name(self):
        raise AttributeError("can't delete attribute 'name'")
