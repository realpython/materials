import csv
import json
from itertools import batched


class TextFileReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as f:
            result = []
            for batch in batched(f.readlines(), 3):
                record = {}
                record["name"] = batch[0].strip()
                record["age"] = batch[1].strip()
                record["job"] = batch[2].strip()
                result.append(record)
            return result


class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as f:
            return list(csv.DictReader(f))


class JSONReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as f:
            return json.load(f)


readers = [
    TextFileReader("file.txt"),
    CSVReader("file.csv"),
    JSONReader("file.json"),
]

for reader in readers:
    print(reader.read())
