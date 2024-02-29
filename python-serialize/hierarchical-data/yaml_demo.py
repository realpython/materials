import json

import yaml


def main():
    yaml_data = serialize()
    print(yaml_data)
    print(deserialize(yaml_data))


def serialize():
    with open("data/training.json", encoding="utf-8") as file:
        document = json.load(file)
        return yaml.safe_dump(document)


def deserialize(data):
    return yaml.safe_load(data)


if __name__ == "__main__":
    main()
