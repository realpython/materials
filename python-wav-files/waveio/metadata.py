from dataclasses import dataclass
from functools import cached_property

from waveio.encoding import PCMEncoding


@dataclass(frozen=True)
class WaveMetadata:
    encoding: PCMEncoding
    frames_per_second: float
    num_channels: int
    num_frames: int | None = None

    @cached_property
    def num_seconds(self):
        return self.num_frames / self.frames_per_second
