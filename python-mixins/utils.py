from collections import UserDict


class DebugMixin:
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        print(f"Item set: {key=!r}, {value=!r}")

    def __delitem__(self, key):
        super().__delitem__(key)
        print(f"Item deleted: {key=!r}")


class CaseInsensitiveDict(DebugMixin, UserDict):
    def __setitem__(self, key: str, value: str) -> None:
        super().__setitem__(key.lower(), value)

    def __getitem__(self, key: str) -> str:
        return super().__getitem__(key.lower())

    def __delitem__(self, key: str) -> None:
        super().__delitem__(key.lower())

    def __contains__(self, key: str) -> bool:
        return super().__contains__(key.lower())

    def get(self, key: str, default: str = "") -> str:
        return super().get(key.lower(), default)


if __name__ == "__main__":
    from pprint import pp

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Cookie"] = "csrftoken=a4f3c7d28c194e5b; sessionid=f92e4b7c6"

    print(f"{headers["cookie"] = }")
    print(f"{"CooKIE" in headers = }")

    del headers["Cookie"]
    print(f"{headers = }")

    pp(CaseInsensitiveDict.__mro__)
