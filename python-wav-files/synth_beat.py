import math
import wave

FRAMES_PER_SECOND = 44100


def beat(frequency1, frequency2, num_seconds):
    for frame in range(round(num_seconds * FRAMES_PER_SECOND)):
        time = frame / FRAMES_PER_SECOND
        amplitude1 = math.sin(2 * math.pi * frequency1 * time)
        amplitude2 = math.sin(2 * math.pi * frequency2 * time)
        amplitude = max(-1, min(amplitude1 + amplitude2, 1))
        yield round((amplitude + 1) / 2 * 255)


with wave.open("output.wav", mode="wb") as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(1)
    wav_file.setframerate(FRAMES_PER_SECOND)
    wav_file.writeframes(bytes(beat(440, 441, 2.5)))
