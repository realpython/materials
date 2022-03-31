import subprocess


def get_char(process):
    character = process.stdout.read(1)
    print(
        character,
        end="",
        flush=True,  # So display is the same as running it directly
    )
    return character


def search_for_output(string, process):
    buffer = ""
    while True:
        buffer = buffer + get_char(process)
        if string in buffer:
            return


with subprocess.Popen(
    [
        "python",
        "-u",  # So display is the same as running it directly
        "choice_react.py",
    ],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
) as process:

    buffer = ""

    search_for_output("when you are ready\n", process)
    process.stdin.write("\n")
    process.stdin.flush()
    search_for_output("==\n= ", process)
    stdout, stderr = process.communicate(f"{get_char(process)}\n", timeout=10)
    print(stdout)


print(process)
