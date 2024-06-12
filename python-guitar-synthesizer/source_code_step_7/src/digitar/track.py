import numpy as np

from digitar.temporal import Hertz, Time


class AudioTrack:
    def __init__(self, sampling_rate: Hertz) -> None:
        self.sampling_rate = int(sampling_rate)
        self.samples = np.array([], dtype=np.float64)

    def __len__(self) -> int:
        return self.samples.size

    @property
    def duration(self) -> Time:
        return Time(seconds=len(self) / self.sampling_rate)

    def add(self, samples: np.ndarray) -> None:
        self.samples = np.append(self.samples, samples)

    def add_at(self, instant: Time, samples: np.ndarray) -> None:
        samples_offset = round(instant.seconds * self.sampling_rate)
        if samples_offset == len(self):
            self.add(samples)
        elif samples_offset > len(self):
            self.add(np.zeros(samples_offset - len(self)))
            self.add(samples)
        else:
            end = samples_offset + len(samples)
            if end > len(self):
                self.add(np.zeros(end - len(self)))
            self.samples[samples_offset:end] += samples
