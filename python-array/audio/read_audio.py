import wave
from array import array

with wave.open("PCM_24_bit_signed.wav", mode="rb") as wave_file:
    if wave_file.getsampwidth() == 3:
        raw_bytes = wave_file.readframes(wave_file.getnframes())
        samples = array(
            "i",
            (
                int.from_bytes(
                    raw_bytes[i : i + 3],
                    byteorder="little",
                    signed=True,
                )
                for i in range(0, len(raw_bytes), 3)
            ),
        )

print(f"{len(raw_bytes) = }")
print(f"{len(samples) = }")
print(f"{wave_file.getnframes() = }")
print(f"{samples.itemsize = }")
print(f"{samples.itemsize * len(samples) = }")
