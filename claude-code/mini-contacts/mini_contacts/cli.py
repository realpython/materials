import argparse
import sys

from mini_contacts import storage


def _print_table(contacts: list[dict[str, str]]) -> None:
    if not contacts:
        print("No contacts found.")
        return
    headers = {"name": "Name", "email": "Email", "phone": "Phone"}
    widths = {
        field: max(len(headers[field]), max(len(row[field]) for row in contacts))
        for field in storage.FIELDNAMES
    }
    header_line = " | ".join(headers[f].ljust(widths[f]) for f in storage.FIELDNAMES)
    separator = "-+-".join("-" * widths[f] for f in storage.FIELDNAMES)
    print(header_line)
    print(separator)
    for row in contacts:
        print(" | ".join(row[f].ljust(widths[f]) for f in storage.FIELDNAMES))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Minimal contact manager")
    parser.add_argument(
        "--path", default="~/.mini-contacts.csv", help="Path to the CSV file"
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True
    add_parser = subparsers.add_parser("add", help="Add a new contact")
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument("--email", required=True)
    add_parser.add_argument("--phone", required=True)
    subparsers.add_parser("list", help="List all contacts")
    args = parser.parse_args(argv)

    try:
        if args.command == "add":
            storage.add_contact(args.path, args.name, args.email, args.phone)
            print(f"Added contact: {args.name}")
        elif args.command == "list":
            contacts = storage.read_contacts(args.path)
            _print_table(contacts)
    except (ValueError, OSError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
