import re
from functools import cached_property

from pytest import Config


class Readme:
    def __init__(self, config: Config) -> None:
        path = config.rootpath / "README.md"
        if path.exists():
            self._content = path.read_text(encoding="utf-8")
        else:
            self._content = ""
        self._folder_name = config.rootpath.name

    @cached_property
    def exercise_name(self) -> str:
        if match := re.search(r"^# (.+)", self._content):
            return match.group(1).title()
        else:
            return self._folder_name.title()
