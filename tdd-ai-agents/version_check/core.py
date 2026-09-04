import re
from functools import total_ordering

_VERSION = re.compile(
    r"^\s*(?P<release>\d+(?:\.\d+)*)"
    r"(?:(?P<pre_label>a|b|rc)(?P<pre_num>\d+))?"
    r"(?:\.post(?P<post>\d+))?"
    r"(?:\.dev(?P<dev>\d+))?\s*$"
)
_PRE_ORDER = {"a": 0, "b": 1, "rc": 2}


@total_ordering
class Version:
    def __init__(self, text):
        match = _VERSION.match(text)
        if match is None:
            raise ValueError(f"invalid version string: {text!r}")
        self._release = tuple(
            int(part) for part in match["release"].split(".")
        )
        if match["pre_label"] is not None:
            self._pre = (_PRE_ORDER[match["pre_label"]], int(match["pre_num"]))
        else:
            self._pre = None
        self._post = int(match["post"]) if match["post"] else None
        self._dev = int(match["dev"]) if match["dev"] else None

    def _key(self):
        if self._dev is not None and self._pre is None:
            phase = (0, self._dev)
        elif self._pre is not None:
            phase = (1, self._pre)
        elif self._post is not None:
            phase = (3, self._post)
        else:
            phase = (2, 0)
        return (self._release, phase)

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._key() == other._key()

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._key() < other._key()
