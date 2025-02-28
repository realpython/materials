import random
import time


def read_temperature():
    return random.uniform(20.0, 30.0)


while True:
    temperature = read_temperature()
    print(f"Temperature: {temperature:.2f}°C")

    if temperature >= 28:
        print("Required temperature reached! Stopping monitoring.")
        break

    time.sleep(1)
