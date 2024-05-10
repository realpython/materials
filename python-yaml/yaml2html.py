# yaml2html.py

import sys

import yaml
from yaml import (
    MappingEndEvent,
    MappingStartEvent,
    ScalarEvent,
    SequenceEndEvent,
    SequenceStartEvent,
)

OPEN_TAG_EVENTS = (ScalarEvent, SequenceStartEvent, MappingStartEvent)
CLOSE_TAG_EVENTS = (ScalarEvent, SequenceEndEvent, MappingEndEvent)


class HTMLBuilder:
    def __init__(self):
        self._context = []
        self._html = []

    @property
    def html(self):
        return "".join(self._html)

    def process(self, event):

        if isinstance(event, OPEN_TAG_EVENTS):
            self._handle_tag()

        if isinstance(event, ScalarEvent):
            self._html.append(event.value)
        elif isinstance(event, SequenceStartEvent):
            self._html.append("<ul>")
            self._context.append(list)
        elif isinstance(event, SequenceEndEvent):
            self._html.append("</ul>")
            self._context.pop()
        elif isinstance(event, MappingStartEvent):
            self._html.append("<dl>")
            self._context.append(0)
        elif isinstance(event, MappingEndEvent):
            self._html.append("</dl>")
            self._context.pop()

        if isinstance(event, CLOSE_TAG_EVENTS):
            self._handle_tag(close=True)

    def _handle_tag(self, close=False):
        if len(self._context) > 0:
            if self._context[-1] is list:
                self._html.append("</li>" if close else "<li>")
            else:
                if self._context[-1] % 2 == 0:
                    self._html.append("</dt>" if close else "<dt>")
                else:
                    self._html.append("</dd>" if close else "<dd>")
                if close:
                    self._context[-1] += 1


def yaml2html(stream, loader=yaml.SafeLoader):
    builder = HTMLBuilder()
    for event in yaml.parse(stream, loader):
        builder.process(event)
        if isinstance(event, yaml.DocumentEndEvent):
            yield builder.html
            builder = HTMLBuilder()


if __name__ == "__main__":
    print("".join(yaml2html("".join(sys.stdin.readlines()))))
