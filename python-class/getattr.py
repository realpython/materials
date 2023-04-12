class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def __getattr__(self, attr):
        return getattr(self, attr)
