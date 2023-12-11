from fastavro import reader, writer
from fastavro.schema import load_schema
from models import User


def main():
    serialize("users.avro", "user.asvc")
    for user in deserialize("users.avro"):
        print(user)


def serialize(filename, schema_filename):
    users = [User.fake() for _ in range(5)]
    with open(filename, mode="wb") as file:
        schema = load_schema(schema_filename)
        writer(file, schema, [user._asdict() for user in users])


def deserialize(filename):
    with open(filename, mode="rb") as file:
        for record in reader(file):
            yield User(**record)


if __name__ == "__main__":
    main()
