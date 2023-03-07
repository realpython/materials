class User:
    __slots__ = ("name", "job")

    def __init__(self, name, job):
        self.name = name
        self.job = job
