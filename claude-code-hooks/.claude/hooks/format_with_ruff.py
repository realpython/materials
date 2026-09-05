import json
import subprocess
import sys
from pathlib import Path


def main():
    event = json.load(sys.stdin)
    if event.get("tool_name") not in {"Write", "Edit"}:
        return 0
    file_path = event.get("tool_input", {}).get("file_path", "")
    if not file_path.endswith(".py") or not Path(file_path).exists():
        return 0
    subprocess.run(["ruff", "check", "--fix", file_path], check=False)
    subprocess.run(["ruff", "format", file_path], check=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
