# blacklist_importer.py

import sys

BLACKLISTED_MODULES = {"re"}


class BlacklistFinder:
    @classmethod
    def find_spec(cls, name, path, target=None):
        if name in BLACKLISTED_MODULES:
            raise ModuleNotFoundError(f"{name!r} is blacklisted")


sys.meta_path.insert(0, BlacklistFinder)
