import yaml
from models import User


def main():
    user_yaml = serialize()
    user = deserialize(user_yaml)
    print(user_yaml)
    print(user)


def serialize():
    user = User(name="John", password="*%!U8n9erx@GdqK(@J")
    return yaml.dump(user)


def deserialize(yaml_data):
    return yaml.unsafe_load(yaml_data)


if __name__ == "__main__":
    main()
