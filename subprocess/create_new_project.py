import subprocess
import os
from pathlib import Path, PurePath
import venv


def create_new_project(name):

    project_folder = PurePath.joinpath(Path.cwd(), name)
    project_folder.mkdir()
    os.chdir(project_folder)  # Should change to call git with -C flag
    # which would mean that this line would not be needed
    project_folder.joinpath("README.md").touch()
    project_folder.joinpath(".gitignore").touch()
    with open(".gitignore", mode="w") as f:
        f.write("\n".join(["venv", "__pycache__"]))
    venv.create("venv", system_site_packages=True, with_pip=True)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "first commit"])

    # Activating venv? Would need access to parent process of Python?


if __name__ == "__main__":
    create_new_project("test")
