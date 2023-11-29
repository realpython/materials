import array
import pickle


def main():
    serialize(data=255, filename="data.pkl")
    data = deserialize("data.pkl")
    print(data)
    print(pickle.dumps(data))
    print(pickle.loads(b"\x80\x05K\xff."))
    print(pickle.loads(array.array("B", [128, 4, 75, 255, 46])))


def serialize(data, filename):
    with open(filename, mode="wb") as file:
        pickle.dump(data, file)


def deserialize(filename):
    with open(filename, mode="rb") as file:
        return pickle.load(file)


if __name__ == "__main__":
    main()
