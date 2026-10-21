import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Note:
    title: str
    body: str = ""


class NoteStore:
    """Keep notes in memory and persist them to a JSON file."""

    def __init__(self, path):
        self.path = Path(path)
        self.notes = self._load()

    def _load(self):
        if not self.path.exists():
            return []
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [Note(**item) for item in data]

    def add(self, title):
        note = Note(title)
        self.notes.append(note)
        return note

    def save(self):
        data = [asdict(note) for note in self.notes]
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")
