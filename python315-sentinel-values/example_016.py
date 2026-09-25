import inspect

from settings_sentinel import get_setting

help(get_setting)
print(inspect.signature(get_setting))
