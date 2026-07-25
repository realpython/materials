import json
import sys


def main():
    event = json.load(sys.stdin)
    if event.get("tool_name") != "Bash":
        return 0
    command = event.get("tool_input", {}).get("command", "")
    words = command.split()
    for i, word in enumerate(words[:-1]):
        if word not in {"pip", "pip3"} or words[i + 1] != "install":
            continue
        if i > 0 and words[i - 1] == "uv":
            continue  # uv pip install is fine
        print("Use 'uv add' instead of pip install.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
