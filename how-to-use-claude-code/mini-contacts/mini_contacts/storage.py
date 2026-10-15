import csv
import os

FIELDNAMES = ("name", "email", "phone")


def read_contacts(path: str) -> list[dict[str, str]]:
    path = os.path.expanduser(path)
    try:
        with open(path, newline="") as f:
            reader = csv.DictReader(f, restval="")
            if reader.fieldnames is None:
                return []
            if tuple(reader.fieldnames) != FIELDNAMES:
                raise ValueError(
                    f"Expected CSV headers {FIELDNAMES}, got {tuple(reader.fieldnames)}"
                )
            return list(reader)
    except FileNotFoundError:
        return []


def add_contact(path: str, name: str, email: str, phone: str) -> None:
    if not all([name, email, phone]):
        raise ValueError("name, email, and phone must not be empty")
    path = os.path.expanduser(path)
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow({"name": name, "email": email, "phone": phone})
