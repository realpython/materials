class Registry(type):
    names = []

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        Registry.names.append(name)
        return cls


class Plugin(metaclass=Registry):
    pass


class CSVExport(Plugin):
    pass


print(Registry.names)
print(type(CSVExport).__name__)
