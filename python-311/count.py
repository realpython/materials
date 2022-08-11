import sys
import time

import colorama
from colorama import Cursor

colorama.init()


def print_at(row, text):
    print(Cursor.POS(1, 1 + row) + str(text))
    time.sleep(0.03)


def count_lines_in_file(file_num, file_name):
    counter_text = f"{file_name[:20]:<20} "
    with open(file_name, mode="rt", encoding="utf-8") as file:
        for line_num, _ in enumerate(file, start=1):
            counter_text += "□"
            print_at(file_num, counter_text)
        print_at(file_num, f"{counter_text} ({line_num})")


def count_all_files(file_names):
    for file_num, file_name in enumerate(file_names, start=1):
        count_lines_in_file(file_num, file_name)


if __name__ == "__main__":
    print(colorama.ansi.clear_screen())
    count_all_files(sys.argv[1:])
    print(Cursor.POS(1, 1 + len(sys.argv)))
