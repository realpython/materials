import pickle

from models import User


def main():
    data = serialize(User("alice", "secret"))
    user = deserialize(data)
    print(data)
    print(user)


def serialize(user):
    return pickle.dumps(user)


def deserialize(data):
    return pickle.loads(data)


if __name__ == "__main__":
    main()
