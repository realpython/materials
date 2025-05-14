import random


def check_speed_limit(limit=80):
    speed = read_speedometer()
    if speed > limit:
        print("You are over the speed limit! Slow down.")


def read_speedometer():
    speed = random.randint(30, 130)
    print(f"Speedometer reading: {speed} km/h")
    return speed


check_speed_limit()
