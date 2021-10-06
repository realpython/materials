from microbit import display, Image, accelerometer, sleep
from random import randrange

# Define left, stay still and right
directions = ["L", "O", "R"]
points = 0

# While the micro:bit is on
while True:
    # Pick a random direction
    direction = directions[randrange(3)]
    display.show(direction)
    # Sleep for a second (1000ms)
    sleep(1000)

    # Get the X-axis (left-right) tilt
    acc_x = accelerometer.get_x()
    # Determine direction
    if acc_x < -200:
        player_in = "L"
    elif abs(acc_x) < 200:
        player_in = "O"
    elif acc_x > 200:
        player_in = "R"

    # Check win condition
    if player_in == direction:
        # Player's input is correct
        points += 1
    else:
        display.scroll(points)
        display.show(Image.SAD)
        points = 0
        sleep(1000)
