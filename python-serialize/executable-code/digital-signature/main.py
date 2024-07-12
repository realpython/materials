import pickle
from pathlib import Path

from trustworthy import safe_dump, safe_load


def main():
    path = Path("code.pkl")
    serialize(lambda a, b: a + b, path, b"top-secret")
    code = deserialize(path, b"top-secret")
    print(code)
    print(f"{code(3, 2) = }")
    try:
        deserialize(path, b"incorrect-key")
    except pickle.UnpicklingError as ex:
        print(repr(ex))


def serialize(code, path, secret_key):
    with path.open(mode="wb") as file:
        safe_dump(code, file, secret_key)


def deserialize(path, secret_key):
    with path.open(mode="rb") as file:
        return safe_load(file, secret_key)


if __name__ == "__main__":
    main()
