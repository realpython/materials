"""Hot-reload the scenery in a background thread."""

import itertools
import threading
import time

from pretzel import assets

BACKGROUNDS = ["bakery_dawn.ppm", "bakery_noon.ppm", "bakery_dusk.ppm"]


class BackgroundStreamer(threading.Thread):
    def __init__(self, fast=False, interval=2.0):
        super().__init__(name="background-streamer", daemon=True)
        self._names = itertools.cycle(BACKGROUNDS)
        self._fast = fast
        self._interval = interval
        self._lock = threading.Lock()
        self._current = assets.load_background(next(self._names), fast)

    @property
    def background(self):
        with self._lock:
            return self._current

    def run(self):
        while True:
            time.sleep(self._interval)
            fresh = assets.load_background(next(self._names), self._fast)
            with self._lock:
                self._current = fresh
