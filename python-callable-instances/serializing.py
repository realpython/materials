import json

import yaml


class JsonSerializer:
    def __call__(self, data):
        return json.dumps(data, indent=4)


class YamlSerializer:
    def __call__(self, data):
        return yaml.dump(data)


class DataSerializer:
    def __init__(self, serializer_strategy):
        self.serializer_strategy = serializer_strategy

    def serialize(self, data):
        return self.serializer_strategy(data)
