import csv
import json
from itertools import batched  # Python >= 3.12


class TextReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, encoding="utf-8") as file:
            return [
                {
                    "name": batch[0].strip(),
                    "age": batch[1].strip(),
                    "job": batch[2].strip(),
                }
                for batch in batched(file.readlines(), 3)
            ]


class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))


class JSONReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, encoding="utf-8") as file:
            return json.load(file)
