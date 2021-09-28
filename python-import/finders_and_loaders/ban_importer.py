# ban_importer.py

import sys

BANNED_MODULES = {"re"}


class BanFinder:
    @classmethod
    def find_spec(cls, name, path, target=None):
        if name in BANNED_MODULES:
            raise ModuleNotFoundError(f"{name!r} is banned")


sys.meta_path.insert(0, BanFinder)
