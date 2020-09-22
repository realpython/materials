# local/serializers/yaml.py

import yaml
from serializers.json import JsonSerializer


class YamlSerializer(JsonSerializer):
    def __str__(self):
        return yaml.dump(self._current_object)
