import csv
from collections import Counter
from io import TextIOWrapper


def process_hotspots(file: str | TextIOWrapper):
    hotspots = []

    if isinstance(file, str):
        with open(file, "r") as csv_file:
            for row in csv.DictReader(csv_file):
                hotspots.append(row["Provider"])
    else:
        with file as csv_file:
            for row in csv.DictReader(csv_file):
                hotspots.append(row["Provider"])

    provider, count = Counter(hotspots).most_common(1)[0]
    print(
        f"There are {len(hotspots)} Wi-Fi hotspots in NYC.\n"
        f"{provider} has the most with {count}."
    )


if __name__ == "__main__":
    process_hotspots("NYC_Wi-Fi_Hotspot_Locations.csv")
