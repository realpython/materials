import csv
import json


class CSVProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, encoding="utf-8", newline="") as file:
            return list(csv.DictReader(file))

    def write(self, data):
        with open(
            self.filename, mode="w", encoding="utf-8", newline=""
        ) as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class JSONProcessor:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, encoding="utf-8") as file:
            return json.load(file)

    def write(self, data):
        with open(self.filename, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)


class FileProcessor:
    def __init__(self, filename, processor):
        self.filename = filename
        self.processor = processor(filename)

    def __getattr__(self, attr):
        return getattr(self.processor, attr)


file_proc = FileProcessor("products.csv", CSVProcessor)
print(file_proc.read())
