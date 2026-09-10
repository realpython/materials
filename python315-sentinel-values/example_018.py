import typing
from settings_typed_sentinel import get_setting

hints = typing.get_type_hints(get_setting)
print(hints["default"])
