# countdown.py

import optional_color
from optional_color import Cursor, Fore
import time

optional_color.init(autoreset=True)
countdown = [f"{Fore.BLUE}{n}" for n in range(10, 0, -1)]
countdown.append(f"{Fore.RED}Lift off!")

print(f"{Fore.GREEN}Countdown starting:\n")
for count in countdown:
    time.sleep(1)
    print(f"{Cursor.UP(1)}{count} ")
