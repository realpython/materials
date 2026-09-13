import json
import platform
import subprocess
import sys


def notify(title, message):
    system = platform.system()
    if system == "Darwin":
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(["osascript", "-e", script], check=False)
    elif system == "Linux":
        subprocess.run(["notify-send", title, message], check=False)
    else:
        return False
    return True


def main():
    json.load(sys.stdin)
    try:
        notified = notify("Claude Code", "Claude just finished responding")
    except FileNotFoundError:
        notified = False
    if not notified:
        print("Claude just finished responding")
    return 0


if __name__ == "__main__":
    sys.exit(main())
