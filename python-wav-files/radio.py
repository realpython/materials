import av

from waveio.encoding import PCMEncoding
from waveio.metadata import WaveMetadata


class RadioStream:
    def __init__(self, stream_url):
        self.container = av.open(stream_url)
        self.metadata = get_metadata(self.container)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.container.close()

    def __iter__(self):
        for frame in self.container.decode():
            channels = frame.to_ndarray()
            samples = channels.T.reshape(-1)
            yield self.metadata.encoding.encode(samples)


def get_metadata(container):
    (audio_stream,) = container.streams.audio
    num_channels = audio_stream.channels
    bytes_per_sample = audio_stream.format.bytes // num_channels
    return WaveMetadata(
        encoding=PCMEncoding(bytes_per_sample),
        frames_per_second=audio_stream.rate,
        num_channels=num_channels,
    )
