# pip_importer.py

import subprocess
import sys
from importlib import util


class PipFinder:
    @classmethod
    def find_spec(cls, name, path, target=None):
        print(f"Module {name!r} not installed.  Attempting to pip install")
        cmd = f"{sys.executable} -m pip install {name}"
        try:
            subprocess.run(cmd.split(), check=True)
        except subprocess.CalledProcessError:
            return None

        return util.find_spec(name)


sys.meta_path.append(PipFinder)
