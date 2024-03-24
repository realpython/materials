import itertools
import math
import wave

FRAMES_PER_SECOND = 44100


def sound_wave(frequency, num_seconds):
    for frame in range(round(num_seconds * FRAMES_PER_SECOND)):
        time = frame / FRAMES_PER_SECOND
        amplitude = math.sin(2 * math.pi * frequency * time)
        yield round((amplitude + 1) / 2 * 255)


left_channel = sound_wave(440, 2.5)
right_channel = sound_wave(480, 2.5)
stereo_frames = itertools.chain(*zip(left_channel, right_channel))

with wave.open("output.wav", mode="wb") as wav_file:
    wav_file.setnchannels(2)
    wav_file.setsampwidth(1)
    wav_file.setframerate(FRAMES_PER_SECOND)
    wav_file.writeframes(bytes(stereo_frames))
