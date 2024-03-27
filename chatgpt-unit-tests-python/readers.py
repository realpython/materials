import json


class JSONReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, encoding="utf-8") as file:
            return json.load(file)
