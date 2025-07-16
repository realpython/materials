def key_type(expected_type):
    def class_decorator(cls):
        setitem = cls.__setitem__

        def __setitem__(self, key, value):
            if not isinstance(key, expected_type):
                raise TypeError(
                    f"key must be {expected_type} but was {type(key)}"
                )
            return setitem(self, key, value)

        cls.__setitem__ = __setitem__
        return cls

    return class_decorator


def value_type(expected_type):
    def class_decorator(cls):
        setitem = cls.__setitem__

        def __setitem__(self, key, value):
            if not isinstance(value, expected_type):
                raise TypeError(
                    f"value must be {expected_type} but was {type(value)}"
                )
            return setitem(self, key, value)

        cls.__setitem__ = __setitem__
        return cls

    return class_decorator


if __name__ == "__main__":
    from collections import UserDict

    @key_type(str)
    @value_type(int)
    class Inventory(UserDict):
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
