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
    elif system == "Windows":
        toast = f"New-BurntToastNotification -Text '{title}', '{message}'"
        subprocess.run(
            ["powershell", "-NoProfile", "-Command", toast], check=False
        )


def main():
    json.load(sys.stdin)
    try:
        notify("Claude Code", "Claude just finished responding")
    except FileNotFoundError:
        print("Claude just finished responding")
    return 0


if __name__ == "__main__":
    sys.exit(main())
