# debug_importer.py

import sys


class DebugFinder:
    @classmethod
    def find_spec(cls, name, path, target=None):
        print(f"Importing {name!r}")
        return None


sys.meta_path.insert(0, DebugFinder)
