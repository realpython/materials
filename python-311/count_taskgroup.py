import asyncio
import sys

import colorama
from colorama import Cursor

colorama.init()


async def print_at(row, text):
    print(Cursor.POS(1, 1 + row) + str(text))
    await asyncio.sleep(0.03)


async def count_lines_in_file(file_num, file_name):
    counter_text = f"{file_name[:20]:<20} "
    with open(file_name, mode="rt", encoding="utf-8") as file:
        for line_num, _ in enumerate(file, start=1):
            counter_text += "□"
            await print_at(file_num, counter_text)
    await print_at(file_num, f"{counter_text} ({line_num})")
    if line_num == 13:
        raise RuntimeError("Files with thirteen lines are too scary!")


async def safe_count_lines_in_file(file_num, file_name):
    try:
        await count_lines_in_file(file_num, file_name)
    except Exception as err:
        await print_at(file_num, err)


async def count_all_files(file_names):
    async with asyncio.TaskGroup() as tg:
        for file_num, file_name in enumerate(file_names, start=1):
            tg.create_task(safe_count_lines_in_file(file_num, file_name))


if __name__ == "__main__":
    print(colorama.ansi.clear_screen())
    asyncio.run(count_all_files(sys.argv[1:]))
    print(Cursor.POS(1, 1 + len(sys.argv)))
