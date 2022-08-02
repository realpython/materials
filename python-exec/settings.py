# settings.py

from pathlib import Path


def load_config(config_file):
    config_file = Path(config_file)
    code = compile(config_file.read_text(), config_file.name, "exec")
    config_dict = {}
    exec(code, {"__builtins__": {}}, config_dict)
    return config_dict
