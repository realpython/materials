import pathlib
from pprint import pp

cwd = pathlib.Path("My Documents")

pp(list(cwd.glob("*")))

pp(list(cwd.glob("**/*")))

pp(list(cwd.glob("**/*.py")))
pp(list(cwd.rglob("*.py")))

pp([file for file in cwd.glob("**/*") if file.suffix in [".py", ".md"]])

pp([file for file in cwd.glob("**/*") if file.is_dir])
