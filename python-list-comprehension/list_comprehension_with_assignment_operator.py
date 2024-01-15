import random


def get_weather_data():
    return random.randrange(90, 110)


hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps)
