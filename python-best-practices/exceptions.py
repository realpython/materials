# Avoid this:
# import json


# def load_config(path):
#     try:
#         with open(path, encoding="utf-8") as config:
#             data = json.load(config)
#     except Exception:
#         # If something went wrong, return an empty config
#         return {}
#     return data


# def main():
#     try:
#         config = load_config("settings.json")
#     except Exception:
#         print("Sorry, something went wrong.")
#     # Do something with config...


# Favor this:
import json
import logging

log = logging.getLogger(__name__)


class ConfigError(Exception):
    """Raised when issues occur with config file."""


def load_config(path):
    try:
        with open(path, encoding="utf-8") as config:
            data = json.load(config)
    except FileNotFoundError as error:
        raise ConfigError(f"Config file not found: {path}") from error
    except json.JSONDecodeError as error:
        raise ConfigError(f"Invalid JSON: {path}") from error
    return data


def main():
    try:
        config = load_config("settings.json")
        print("Config:", config)
    except ConfigError as error:
        log.error("Error loading the config: %s", error)
        print("Sorry, something went wrong while loading the settings.")
    # Do something with config...
