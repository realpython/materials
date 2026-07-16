"""Record per-frame timings to a log file that survives crashes."""

import os


class FrameLog:
    def __init__(self, path, durable=True):
        self.durable = durable
        self._file = open(path, "w", encoding="utf-8")

    def record(self, frame, elapsed_ms):
        self._file.write(f"{frame},{elapsed_ms:.3f}\n")
        if self.durable:
            self._file.flush()
            os.fsync(self._file.fileno())

    def close(self):
        self._file.close()
