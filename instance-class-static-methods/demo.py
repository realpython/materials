class DemoClass:
    def instance_method(self):
        return ("instance method called", self)

    @classmethod
    def class_method(cls):
        return ("class method called", cls)

    @staticmethod
    def static_method():
        return ("static method called",)


if __name__ == "__main__":
    obj = DemoClass()
    print(obj.instance_method())
    print(obj.class_method())
    print(obj.static_method())
