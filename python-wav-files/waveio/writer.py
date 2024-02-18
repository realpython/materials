import wave

import numpy as np


class WAVWriter:
    def __init__(self, metadata, path):
        self.metadata = metadata
        self._wav_file = wave.open(str(path), mode="wb")
        self._wav_file.setframerate(metadata.frames_per_second)
        self._wav_file.setnchannels(metadata.num_channels)
        self._wav_file.setsampwidth(metadata.encoding)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self._wav_file.close()

    def append_channels(self, *channels):
        match channels:
            case [combined] if combined.ndim > 1:
                self.append_amplitudes(combined.T.reshape(-1))
            case _:
                self.append_amplitudes(np.dstack(channels).reshape(-1))

    def append_amplitudes(self, amplitudes):
        frames = self.metadata.encoding.encode(amplitudes)
        self._wav_file.writeframes(frames)
