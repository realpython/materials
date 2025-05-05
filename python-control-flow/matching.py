import csv
import json
from pathlib import Path


def read_file(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"File not found: {file_path}")
        return None

    with path.open(mode="r", encoding="utf-8") as file:
        match path.suffix.lower():
            case ".json":
                data = json.load(file)
                print("Loaded JSON data.")
                return data
            case ".csv":
                reader = csv.DictReader(file)
                data = list(reader)
                print("Loaded CSV data.")
                return data
            case _:
                print(f"Unsupported file type: {path.suffix}")
                return None


for file_path in ["test.json", "test.csv", "test.toml", "test.txt"]:
    result = read_file(file_path)
    print(result)
