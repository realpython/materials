import csv

from models import User


def main():
    serialize("users.csv")
    for user in deserialize("users.csv"):
        print(user)


def serialize(filename):
    users = [User.fake() for _ in range(50)]
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(users)


def deserialize(filename):
    with open(filename, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, fieldnames=User._fields)
        return [User.from_dict(row_dict) for row_dict in reader]


if __name__ == "__main__":
    main()
