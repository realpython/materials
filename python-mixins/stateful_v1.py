class TypedKeyMixin:
    key_type = object

    def __setitem__(self, key, value):
        if not isinstance(key, self.key_type):
            raise TypeError(f"key must be {self.key_type} but was {type(key)}")
        super().__setitem__(key, value)


class TypedValueMixin:
    value_type = object

    def __setitem__(self, key, value):
        if not isinstance(value, self.value_type):
            raise TypeError(
                f"value must be {self.value_type} but was {type(value)}"
            )
        super().__setitem__(key, value)


if __name__ == "__main__":
    from collections import UserDict

    class Inventory(TypedKeyMixin, TypedValueMixin, UserDict):
        key_type = str
        value_type = int

    fruits = Inventory()
    fruits["apples"] = 42

    try:
        fruits["🍌".encode("utf-8")] = 15
    except TypeError as ex:
        print(ex)

    try:
        fruits["bananas"] = 3.5
    except TypeError as ex:
        print(ex)

    print(f"{vars(fruits) = }")
