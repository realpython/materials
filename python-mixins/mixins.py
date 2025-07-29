import json
from typing import Self


class SerializableMixin:
    def serialize(self) -> dict:
        if hasattr(self, "__slots__"):
            return {name: getattr(self, name) for name in self.__slots__}
        else:
            return vars(self)


class JSONSerializableMixin:
    @classmethod
    def from_json(cls, json_string: str) -> Self:
        return cls(**json.loads(json_string))

    def as_json(self) -> str:
        return json.dumps(vars(self))


class TypedKeyMixin:
    def __init__(self, key_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__type = key_type

    def __setitem__(self, key, value):
        if not isinstance(key, self.__type):
            raise TypeError(f"key must be {self.__type} but was {type(key)}")
        super().__setitem__(key, value)


class TypedValueMixin:
    def __init__(self, value_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__type = value_type

    def __setitem__(self, key, value):
        if not isinstance(value, self.__type):
            if not isinstance(value, self.__type):
                raise TypeError(
                    f"value must be {self.__type} but was {type(value)}"
                )
        super().__setitem__(key, value)


if __name__ == "__main__":
    from collections import UserDict
    from dataclasses import dataclass
    from pathlib import Path
    from types import SimpleNamespace

    @dataclass
    class User(JSONSerializableMixin):
        user_id: int
        email: str

    class AppSettings(JSONSerializableMixin, SimpleNamespace):
        def save(self, filepath: str | Path) -> None:
            Path(filepath).write_text(self.as_json(), encoding="utf-8")

    class Inventory(TypedKeyMixin, TypedValueMixin, UserDict):
        pass

    user = User(555, "jdoe@example.com")
    print(user.as_json())

    settings = AppSettings()
    settings.host = "localhost"
    settings.port = 8080
    settings.debug_mode = True
    settings.log_file = None
    settings.urls = (
        "https://192.168.1.200:8000",
        "https://192.168.1.201:8000",
    )
    settings.save("settings.json")

    fruits = Inventory(str, int)
    fruits["apples"] = 42

    try:
        fruits["🍌".encode("utf-8")] = 15
    except TypeError as ex:
        print(ex)

    try:
        fruits["bananas"] = 3.5
    except TypeError as ex:
        print(ex)
