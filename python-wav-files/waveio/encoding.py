from enum import IntEnum

import numpy as np


class PCMEncoding(IntEnum):
    UNSIGNED_8 = 1
    SIGNED_16 = 2
    SIGNED_24 = 3
    SIGNED_32 = 4

    @property
    def max(self):
        return 255 if self == 1 else -self.min - 1

    @property
    def min(self):
        return 0 if self == 1 else -(2 ** (self.num_bits - 1))

    @property
    def num_bits(self):
        return 8 * self

    def decode(self, frames):
        match self:
            case PCMEncoding.UNSIGNED_8:
                return np.frombuffer(frames, "u1") / self.max * 2 - 1
            case PCMEncoding.SIGNED_16:
                return np.frombuffer(frames, "<i2") / -self.min
            case PCMEncoding.SIGNED_24:
                triplets = np.frombuffer(frames, "u1").reshape(-1, 3)
                padded = np.pad(triplets, ((0, 0), (0, 1)), mode="constant")
                samples = padded.flatten().view("<i4")
                samples[samples > self.max] += 2 * self.min
                return samples / -self.min
            case PCMEncoding.SIGNED_32:
                return np.frombuffer(frames, "<i4") / -self.min
            case _:
                raise TypeError("unsupported encoding")

    def encode(self, amplitudes):
        match self:
            case PCMEncoding.UNSIGNED_8:
                samples = np.round((amplitudes + 1) / 2 * self.max)
                return self._clamp(samples).astype("u1").tobytes()
            case PCMEncoding.SIGNED_16:
                samples = np.round(-self.min * amplitudes)
                return self._clamp(samples).astype("<i2").tobytes()
            case PCMEncoding.SIGNED_24:
                samples = np.round(-self.min * amplitudes)
                return (
                    self._clamp(samples)
                    .astype("<i4")
                    .view("u1")
                    .reshape(-1, 4)[:, :3]
                    .flatten()
                    .tobytes()
                )
            case PCMEncoding.SIGNED_32:
                samples = np.round(-self.min * amplitudes)
                return self._clamp(samples).astype("<i4").tobytes()
            case _:
                raise TypeError("unsupported encoding")

    def _clamp(self, samples):
        return np.clip(samples, self.min, self.max)
