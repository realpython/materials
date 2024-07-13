import json


def load_config(config_file):
    with open(config_file) as file:
        config = json.load(file)

    globals().update(config)


load_config("config.json")
print(globals())
