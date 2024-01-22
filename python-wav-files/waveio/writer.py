import wave

import numpy as np


class WaveWriter:
    def __init__(self, metadata, path):
        self.metadata = metadata
        self.file = wave.open(str(path), mode="wb")
        self.file.setframerate(metadata.frames_per_second)
        self.file.setnchannels(metadata.num_channels)
        self.file.setsampwidth(metadata.encoding)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.file.close()

    def append_channels(self, *channels):
        self.append_samples(np.dstack(channels).flatten())

    def append_samples(self, samples):
        self.append_bytes(self.metadata.encoding.encode(samples))

    def append_bytes(self, binary_chunk):
        self.file.writeframes(binary_chunk)
