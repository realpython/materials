import inspect
import wave
from functools import cached_property, wraps

from waveio.encoding import PCMEncoding
from waveio.metadata import WAVMetadata


def reshape(shape):
    if shape not in ("rows", "columns"):
        raise ValueError("Shape must be either 'rows' or 'columns'")

    def decorator(method):
        if inspect.isgeneratorfunction(method):

            @wraps(method)
            def wrapper(self, *args, **kwargs):
                for values in method(self, *args, **kwargs):
                    reshaped = values.reshape(-1, self.metadata.num_channels)
                    yield reshaped if shape == "rows" else reshaped.T

        else:

            @wraps(method)
            def wrapper(self, *args, **kwargs):
                values = method(self, *args, **kwargs)
                reshaped = values.reshape(-1, self.metadata.num_channels)
                return reshaped if shape == "rows" else reshaped.T

        return wrapper

    return decorator


class ArraySlice:
    def __init__(self, values, frames_range):
        self.values = values
        self.frames_range = frames_range

    def __iter__(self):
        return iter(self.values)

    def __getattr__(self, name):
        return getattr(self.values, name)

    def reshape(self, *args, **kwargs):
        reshaped = self.values.reshape(*args, **kwargs)
        return ArraySlice(reshaped, self.frames_range)

    @property
    def T(self):
        return ArraySlice(self.values.T, self.frames_range)


class WAVReader:
    DEFAULT_MAX_FRAMES = 1024

    def __init__(self, path):
        self._wav_file = wave.open(str(path))
        self.metadata = WAVMetadata(
            PCMEncoding(self._wav_file.getsampwidth()),
            self._wav_file.getframerate(),
            self._wav_file.getnchannels(),
            self._wav_file.getnframes(),
        )

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self._wav_file.close()

    @cached_property
    def stereo(self):
        return 2 == self.metadata.num_channels

    @cached_property
    @reshape("rows")
    def frames(self):
        return self._read(self.metadata.num_frames, start_frame=0)

    @cached_property
    @reshape("columns")
    def channels(self):
        return self.frames

    @reshape("columns")
    def channels_sliced(self, start_seconds=0.0, end_seconds=None):
        if end_seconds is None:
            end_seconds = self.metadata.num_seconds
        frames_slice = slice(
            round(self.metadata.frames_per_second * start_seconds),
            round(self.metadata.frames_per_second * end_seconds),
        )
        frames_range = range(*frames_slice.indices(self.metadata.num_frames))
        values = self._read(len(frames_range), frames_range.start)
        return ArraySlice(values, frames_range)

    @reshape("columns")
    def channels_lazy(self, max_frames=DEFAULT_MAX_FRAMES):
        self._wav_file.rewind()
        while True:
            chunk = self._read(max_frames)
            if chunk.size == 0:
                break
            yield chunk

    def _read(self, max_frames=None, start_frame=None):
        if start_frame is not None:
            self._wav_file.setpos(start_frame)
        frames = self._wav_file.readframes(max_frames)
        return self.metadata.encoding.decode(frames)
