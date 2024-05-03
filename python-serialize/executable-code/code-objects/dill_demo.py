import dill


def main():
    create_plus = deserialize(serialize())
    print(create_plus)
    print(f"{create_plus(3)(2) = }")


def serialize():
    import plus

    plus.create_plus.__module__ = None
    return dill.dumps(plus.create_plus, recurse=True)


def deserialize(data):
    return dill.loads(data)


if __name__ == "__main__":
    main()
