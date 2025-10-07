import curses
import time


def main(screen):
    curses.curs_set(0)  # Hide the cursor
    screen.nodelay(True)  # Don't block I/O calls

    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -1),
        curses.KEY_RIGHT: (0, 1),
    }

    direction = directions[curses.KEY_RIGHT]
    snake = [(0, i) for i in reversed(range(20))]

    while True:
        screen.erase()

        # Draw the snake
        screen.addstr(*snake[0], "@")
        for segment in snake[1:]:
            screen.addstr(*segment, "*")

        # Move the snake
        snake.pop()
        snake.insert(
            0, tuple(map(sum, zip(snake[0], direction, strict=False)))
        )

        # Change direction on arrow keystroke
        direction = directions.get(screen.getch(), direction)

        screen.refresh()
        time.sleep(0.1)


if __name__ == "__main__":
    curses.wrapper(main)
