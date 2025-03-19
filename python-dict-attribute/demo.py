class DemoClass:
    class_attr = "This is a class attribute"

    def __init__(self):
        self.instance_attr = "This is an instance attribute"

    def method(self):
        return "This is a method"


print(DemoClass.__dict__)
demo_object = DemoClass()
print(demo_object.__dict__)
