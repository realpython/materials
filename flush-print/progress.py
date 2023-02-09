from time import sleep


def progress(percent=0, width=30):
    progress = width * percent // 100
    bar = "#" * progress
    pad = " " * (width - progress)
    print(f"\r[{bar}{pad}] {percent:.0f}%", end="", flush=True)


for i in range(101):
    progress(i)
    sleep(0.1)
