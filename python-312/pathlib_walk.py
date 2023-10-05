from pathlib import Path

data_path = Path(__file__).parent / "pathlib_walk"


def headline(text):
    print(f"\n{text}\n{'-' * len(text)}")


headline("Using .rglob():")
for path in data_path.rglob("*"):
    print(path)

headline("Using .walk():")
for path, directories, files in data_path.walk():
    print(path, directories, files)

headline("Using .walk(top_down=False):")
for path, directories, files in data_path.walk(top_down=False):
    print(path, directories, files)
