"""Record per-frame timings to a log file that survives crashes."""

import os


class FrameLog:
    def __init__(self, path: str, durable: bool = True) -> None:
        self.durable = durable
        self._file = open(path, "w", encoding="utf-8")

    def record(self, frame: int, elapsed_ms: float) -> None:
        self._file.write(f"{frame},{elapsed_ms:.3f}\n")
        if self.durable:
            self._file.flush()
            os.fsync(self._file.fileno())

    def close(self) -> None:
        self._file.close()
