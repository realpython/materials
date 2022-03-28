import subprocess


process = subprocess.Popen(
    ["python", "simple_react_perf.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

# https://stackoverflow.com/q/57726771
# what-the-difference-between-read-and-read1-in-python

buffer = ""

while True:
    b = process.stdout.read(1)
    if b != "":
        buffer = buffer + b.decode()
    if (
        buffer == "Press enter to play\n"
        or buffer == "Press enter to play\r\n"
    ):
        print(buffer)
        buffer = ""
        process.stdin.write(b"\n")
        process.stdin.flush()

        while True:
            character = process.stdout.read(1)
            print(character.decode(), end="")
            if character.decode() == "g":
                process.stdin.write(b"\n")
                process.stdin.flush()
                break

        break

print(process.stdout.read().decode())


process.kill()
