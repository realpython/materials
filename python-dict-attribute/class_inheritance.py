class Parent:
    def __init__(self):
        self.parent_attr = "parent"


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "child"


parent = Parent()
print(parent.__dict__)

child = Child()
print(child.__dict__)
