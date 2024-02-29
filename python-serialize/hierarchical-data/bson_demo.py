import json

import bson


def main():
    binary_json = serialize()
    print(binary_json)
    print(deserialize(binary_json))


def serialize():
    with open("data/training.json", encoding="utf-8") as file:
        document = json.load(file)
        return bson.encode(document)


def deserialize(data):
    return bson.decode(data)


if __name__ == "__main__":
    main()
