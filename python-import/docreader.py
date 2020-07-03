# docreader.py

import importlib

module_name = input("Name of module? ")
module = importlib.import_module(module_name)
print(module.__doc__)
