from enum import IntEnum

import numpy as np

PCM_U8_MAX = 2**8 - 1
PCM_16_MAX = 2**15 - 1
PCM_24_MAX = 2**23 - 1
PCM_32_MAX = 2**31 - 1


class PCMEncoding(IntEnum):
    UNSIGNED_8 = 1
    SIGNED_16 = 2
    SIGNED_24 = 3
    SIGNED_32 = 4

    def encode(self, normalized_samples):
        match self:
            case PCMEncoding.UNSIGNED_8:
                return (
                    ((normalized_samples + 1) * (PCM_U8_MAX / 2))
                    .astype(np.uint8)
                    .tobytes()
                )
            case PCMEncoding.SIGNED_16:
                return (
                    (normalized_samples * PCM_16_MAX)
                    .astype(np.int16)
                    .tobytes()
                )
            case PCMEncoding.SIGNED_24:
                return b"".join(
                    int(sample).to_bytes(3, byteorder="little", signed=True)
                    for sample in np.clip(
                        normalized_samples * PCM_24_MAX,
                        -PCM_24_MAX - 1,
                        PCM_24_MAX,
                    )
                )
            case PCMEncoding.SIGNED_32:
                return (
                    (normalized_samples * PCM_32_MAX)
                    .astype(np.int32)
                    .tobytes()
                )
            case _:
                raise TypeError("unsupported encoding")

    def decode(self, data):
        match self:
            case PCMEncoding.UNSIGNED_8:
                return (
                    np.frombuffer(data, dtype=np.uint8) / (PCM_U8_MAX / 2)
                ) - 1
            case PCMEncoding.SIGNED_16:
                return np.frombuffer(data, dtype=np.int16) / PCM_16_MAX
            case PCMEncoding.SIGNED_24:
                samples = (
                    int.from_bytes(
                        data[i : i + 3], byteorder="little", signed=True
                    )
                    for i in range(0, len(data), 3)
                )
                return np.fromiter(samples, dtype=np.int32) / PCM_24_MAX
            case PCMEncoding.SIGNED_32:
                return np.frombuffer(data, dtype=np.int32) / PCM_32_MAX
            case _:
                raise TypeError("unsupported encoding")
