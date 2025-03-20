import copy
import json
from pprint import pp


class DataFile:
    def __init__(self, path):
        self.file = open(path, mode="r", encoding="utf-8")

    def __copy__(self):
        return type(self)(self.file.name)

    def __deepcopy__(self, memo):
        return self.__copy__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read_json(self):
        self.file.seek(0)
        return json.load(self.file)


if __name__ == "__main__":
    with DataFile("person.json") as data_file:
        shallow_copy = copy.copy(data_file)
        deep_copy = copy.deepcopy(data_file)
        pp(data_file.read_json())
    print()
    pp(shallow_copy.read_json())
    shallow_copy.file.close()
    print()
    pp(deep_copy.read_json())
    deep_copy.file.close()
