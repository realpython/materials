import importlib
from readers import my_json, my_csv
from importlib import resources

for file in resources.contents("readers"):
    if not file.endswith(".py"):
        continue
    print(file)
    module = importlib.import_module(f"readers.{file.strip('.py')}")
    print(dir(module))
    module.read("")
