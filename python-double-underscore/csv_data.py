# csv_data.py

import csv


class CSVFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        return self._read(delimiter=",")

    def read_tsv(self):
        return self._read(delimiter="\t")

    def _read(self, delimiter):
        with open(self.file_path, mode="r") as file:
            return [row for row in csv.reader(file, delimiter=delimiter)]
