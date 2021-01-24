# csv_importer.py

import csv
import pathlib
import re
import sys
from importlib.machinery import ModuleSpec


class CsvImporter:
    def __init__(self, csv_path):
        """Store path to CSV file"""
        self.csv_path = csv_path

    @classmethod
    def find_spec(cls, name, path, target=None):
        """Look for CSV file"""
        package, _, module_name = name.rpartition(".")
        csv_file_name = f"{module_name}.csv"
        directories = sys.path if path is None else path
        for directory in directories:
            csv_path = pathlib.Path(directory) / csv_file_name
            if csv_path.exists():
                return ModuleSpec(name, cls(csv_path))

    def create_module(self, spec):
        """Returning None uses the standard machinery for creating modules"""
        return None

    def exec_module(self, module):
        """Executing the module means reading the CSV file"""
        # Read CSV data and store as a list of rows
        with self.csv_path.open() as fid:
            rows = csv.DictReader(fid)
            data = list(rows)
            fieldnames = tuple(_identifier(f) for f in rows.fieldnames)

        # Create a dict with each field
        values = zip(*(row.values() for row in data))
        fields = dict(zip(fieldnames, values))

        # Add the data to the module
        module.__dict__.update(fields)
        module.__dict__["data"] = data
        module.__dict__["fieldnames"] = fieldnames
        module.__file__ = str(self.csv_path)

    def __repr__(self):
        """Nice representation of the class"""
        return f"{self.__class__.__name__}({str(self.csv_path)!r})"


def _identifier(var_str):
    """Create a valid identifier from a string

    See https://stackoverflow.com/a/3305731
    """
    return re.sub(r"\W|^(?=\d)", "_", var_str)


# Add the CSV importer at the end of the list of finders
sys.meta_path.append(CsvImporter)
