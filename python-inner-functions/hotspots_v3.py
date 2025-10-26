import csv
from collections import Counter
from io import TextIOWrapper


def process_hotspots(file: str | TextIOWrapper):
    if isinstance(file, str):
        file = open(file, "r")

    with file as csv_file:
        hotspots = [row["Provider"] for row in csv.DictReader(csv_file)]

    provider, count = Counter(hotspots).most_common(1)[0]
    print(
        f"There are {len(hotspots)} Wi-Fi hotspots in NYC.\n"
        f"{provider} has the most with {count}."
    )
