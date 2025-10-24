import csv
from collections import Counter
from io import TextIOWrapper


def process_hotspots(file: str | TextIOWrapper):
    hotspots = []

    def extract_hotspots(csv_file):
        for row in csv.DictReader(csv_file):
            hotspots.append(row["Provider"])

    if isinstance(file, str):
        with open(file, "r") as csv_file:
            extract_hotspots(csv_file)
    else:
        with file as csv_file:
            extract_hotspots(csv_file)

    provider, count = Counter(hotspots).most_common(1)[0]
    print(
        f"There are {len(hotspots)} Wi-Fi hotspots in NYC.\n"
        f"{provider} has the most with {count}."
    )
