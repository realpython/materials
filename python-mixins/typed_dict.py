def typed_dict(key_type=object, value_type=object):
    def class_decorator(cls):
        setitem = cls.__setitem__

        def __setitem__(self, key, value):
            if not isinstance(key, key_type):
                raise TypeError(
                    f"value must be {key_type} but was {type(key)}"
                )

            if not isinstance(value, value_type):
                raise TypeError(
                    f"value must be {value_type} but was {type(value)}"
                )

            setitem(self, key, value)

        cls.__setitem__ = __setitem__

        return cls

    return class_decorator


if __name__ == "__main__":
    from collections import UserDict

    # Enforce str keys and int values:
    @typed_dict(str, int)
    class Inventory(UserDict):
        pass

    # Enforce str keys, allow any value type:
    @typed_dict(str)
    class AppSettings(UserDict):
        pass

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

    settings = AppSettings()
    settings["host"] = "localhost"
    settings["port"] = 8080
    settings["debug_mode"] = True

    try:
        settings[b"binary data"] = "nope"
    except TypeError as ex:
        print(ex)
