import json


def set_config_key(key, value):
    globals()[key] = value


with open("config.json") as json_config:
    for key, value in json.load(json_config).items():
        set_config_key(key, value)
