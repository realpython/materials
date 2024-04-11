import math
import wave
from functools import partial

FRAMES_PER_SECOND = 44100


def sound_wave(frequency, num_seconds):
    for frame in range(round(num_seconds * FRAMES_PER_SECOND)):
        time = frame / FRAMES_PER_SECOND
        amplitude = math.sin(2 * math.pi * frequency * time)
        yield max(-32768, min(round(amplitude * 32768), 32767))


int16 = partial(int.to_bytes, length=2, byteorder="little", signed=True)

left_channel = sound_wave(440, 2.5)
right_channel = sound_wave(480, 2.5)

stereo_frames = bytearray()
for left_sample, right_sample in zip(left_channel, right_channel):
    stereo_frames.extend(int16(left_sample))
    stereo_frames.extend(int16(right_sample))

with wave.open("output.wav", mode="wb") as wav_file:
    wav_file.setnchannels(2)
    wav_file.setsampwidth(2)
    wav_file.setframerate(FRAMES_PER_SECOND)
    wav_file.writeframes(stereo_frames)
