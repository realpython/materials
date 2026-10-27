class Base:
    def setup(self):
        return ["base"]


class Logging(Base):
    def setup(self):
        return super().setup() + ["logging"]


class Metrics(Base):
    def setup(self):
        return super().setup() + ["metrics"]


class Service(Metrics, Logging):
    def setup(self):
        return super().setup() + ["service"]


print(Service().setup())
print([cls.__name__ for cls in Service.__mro__])
