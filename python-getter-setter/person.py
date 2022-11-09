class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self._birth_date = birth_date

    def get_birth_date(self):
        return self._birth_date

    def set_birth_date(self, value, force=False):
        if force:
            self._birth_date = value
        else:
            raise AttributeError("can't set birth_date")
