def TypedKeyMixin(key_type=object):
    class _:
        def __setitem__(self, key, value):
            if not isinstance(key, key_type):
                raise TypeError(f"key must be {key_type} but was {type(key)}")
            super().__setitem__(key, value)

    return _


def TypedValueMixin(value_type=object):
    class _:
        def __setitem__(self, key, value):
            if not isinstance(value, value_type):
                raise TypeError(
                    f"value must be {value_type} but was {type(value)}"
                )
            super().__setitem__(key, value)

    return _


if __name__ == "__main__":
    from collections import UserDict

    class Inventory(TypedKeyMixin(str), TypedValueMixin(int), UserDict):
        key_type = "This attribute has nothing to collide with"

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
    print(f"{Inventory.key_type = }")
