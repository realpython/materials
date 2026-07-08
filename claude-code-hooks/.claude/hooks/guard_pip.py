import json
import sys


def main():
    event = json.load(sys.stdin)
    if event.get("tool_name") != "Bash":
        return 0
    command = event.get("tool_input", {}).get("command", "")
    if "pip install" in command or "pip3 install" in command:
        print("Use 'uv add' instead of pip install.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
