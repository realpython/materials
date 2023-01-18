import importlib
from importlib import resources

print("starting")

for file in resources.contents("readers"):
    if not file.endswith(".py"):
        continue
    print(file)
    module = importlib.import_module(f"readers.{file.strip('.py')}")
    print(dir(module))
    module.read("")
