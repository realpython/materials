import argparse
import csv
from io import StringIO
from pathlib import Path


def csv_to_markdown(
    text: str,
    *,
    delimiter: str = ",",
    header: bool = True,
) -> str:
    raw = text.strip()
    if not raw:
        raise ValueError("CSV text is empty")

    rows = list(csv.reader(StringIO(raw), delimiter=delimiter))
    if not rows:
        raise ValueError("CSV text has no rows")
    if any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("CSV rows do not all have the same number of columns")

    if header:
        headings = [cell.strip() or " " for cell in rows[0]]
        body = rows[1:]
    else:
        headings = [f"Col {index}" for index in range(1, len(rows[0]) + 1)]
        body = rows

    lines = [
        "| " + " | ".join(headings) + " |",
        "| " + " | ".join("---" for _ in headings) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(cell.strip() for cell in row) + " |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a CSV file to a Markdown table."
    )
    parser.add_argument("csv_file", type=Path, help="path to a CSV file")
    parser.add_argument(
        "-d",
        "--delimiter",
        default=",",
        help="field delimiter (default: comma)",
    )
    parser.add_argument(
        "--no-header",
        action="store_true",
        help="treat the first row as data",
    )
    args = parser.parse_args()
    text = args.csv_file.read_text(encoding="utf-8")
    print(
        csv_to_markdown(
            text,
            delimiter=args.delimiter,
            header=not args.no_header,
        ),
        end="",
    )


if __name__ == "__main__":
    main()
