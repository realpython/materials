import json
import sys
from dataclasses import asdict
from datetime import datetime
from typing import Any, Iterator, Protocol, TypedDict

from rich.console import Console, Text
from rich.markdown import Markdown
from rich.panel import Panel

from todolist.status import TaskListStatus


class FormatOptions(TypedDict, total=False):
    indent: int | str | None
    separators: tuple[str, str] | None
    sort_keys: bool


class SupportsWrite[T](Protocol):
    def write(self, data: T, /) -> object: ...


class JSONExporter:
    def __init__(
        self, output: SupportsWrite[str], options: FormatOptions = {}
    ) -> None:
        self.output = output
        self.options = options

    def export(self, content: Any) -> None:
        json.dump(content, self.output, **self.options)


def export_database_to_json() -> None:
    content = list(map(asdict, TaskListStatus.find_all()))
    for exporter in exporters():
        exporter.export(content)


def exporters() -> Iterator[JSONExporter]:
    file = None
    try:
        stdout_exporter = JSONExporter(sys.stdout)
        stdout_exporter.options["indent"] = 2
        stdout_exporter.options["sort_keys"] = False
        stdout_exporter.options["separators"] = (", ", ": ")

        file = open(f"todo_{timestamp()}.json", mode="w+", encoding="utf-8")
        file_exporter = JSONExporter(file)
        file_exporter.options["indent"] = None
        file_exporter.options["sort_keys"] = True
        file_exporter.options["separators"] = (",", ":")

        yield stdout_exporter
        yield file_exporter

        file.seek(0)
        Console(stderr=True).print(
            Panel(
                Markdown(file.read()),
                title=file.name,
                width=80,
                border_style="bold",
            )
        )
    finally:
        if file:
            file.close()


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S")
