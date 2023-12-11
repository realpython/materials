import json


def main():
    data = {"weekend_days": {"Saturday", "Sunday"}}
    json_string = json.dumps(data, default=serialize_custom)
    python_dict = json.loads(json_string, object_hook=deserialize_custom)
    print(repr(json_string))
    print(repr(python_dict))


def serialize_custom(value):
    if isinstance(value, set):
        return {"type": "set", "elements": list(value)}


def deserialize_custom(value):
    match value:
        case {"type": "set", "elements": elements}:
            return set(elements)
        case _:
            return value


if __name__ == "__main__":
    main()
