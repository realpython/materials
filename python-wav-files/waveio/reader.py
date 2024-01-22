import wave
from dataclasses import dataclass
from functools import cached_property

import numpy as np

from waveio.encoding import PCMEncoding
from waveio.metadata import WaveMetadata

type Samples = np.ndarray
type Channels = tuple[Samples, ...]


@dataclass(frozen=True)
class SlicedChannels:
    channels: Channels
    begin_seconds: float
    end_seconds: float

    def __len__(self):
        return len(self.channels)

    def __iter__(self):
        return iter(self.channels)

    @property
    def duration_seconds(self):
        return self.end_seconds - self.begin_seconds

    @property
    def num_samples(self):
        return len(self.channels[0])

    @property
    def x_range(self):
        return np.arange(
            self.begin_seconds,
            self.end_seconds,
            self.duration_seconds / self.num_samples,
        )


class WaveReader:
    DEFAULT_MAX_FRAMES = 4096

    def __init__(self, path):
        self._file = wave.open(str(path))
        self.metadata = get_metadata(self._file)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self._file.close()

    def __iter__(self):
        for channels in self.channels_lazy():
            yield from zip(*channels)

    @property
    def stereo(self):
        return self.metadata.num_channels == 2

    @cached_property
    def channels(self):
        return self._unpack(self._read())

    def channels_lazy(self, max_frames=DEFAULT_MAX_FRAMES):
        return map(self._unpack, self._read_chunks(max_frames))

    def channels_sliced(self, begin_seconds=0.0, end_seconds=None):
        if begin_seconds < 0:
            begin_seconds += self.metadata.num_seconds

        if end_seconds is None:
            end_seconds = self.metadata.num_seconds
        elif end_seconds < 0:
            end_seconds += self.metadata.num_seconds

        if begin_seconds > end_seconds:
            begin_seconds, end_seconds = end_seconds, begin_seconds

        start_frame = round(begin_seconds * self.metadata.frames_per_second)
        stop_frame = round(end_seconds * self.metadata.frames_per_second)

        self._file.setpos(start_frame)
        binary_chunk = self._file.readframes(stop_frame - start_frame)
        channels = self._unpack(self.metadata.encoding.decode(binary_chunk))

        return SlicedChannels(channels, begin_seconds, end_seconds)

    def _read(self):
        self._file.rewind()
        binary_data = self._file.readframes(self.metadata.num_frames)
        return self.metadata.encoding.decode(binary_data)

    def _read_chunks(self, max_frames):
        self._file.rewind()
        while binary_chunk := self._file.readframes(max_frames):
            yield self.metadata.encoding.decode(binary_chunk)

    def _unpack(self, data):
        return tuple(
            data[i :: self.metadata.num_channels]
            for i in range(self.metadata.num_channels)
        )


def get_metadata(wave_file):
    return WaveMetadata(
        PCMEncoding(wave_file.getsampwidth()),
        wave_file.getframerate(),
        wave_file.getnchannels(),
        wave_file.getnframes(),
    )
