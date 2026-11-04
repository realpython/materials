"""Fail when a diff looks like an agent run went off the rails.

Without arguments, check the staged diff (pre-commit mode).
With --base REF, check REF...HEAD (CI mode).
"""

import argparse
import subprocess
import sys

MAX_CHANGED_LINES = 200
IGNORED = ("uv.lock",)
PROTECTED = (
    ".github/",
    ".pre-commit-config.yaml",
    "pyproject.toml",
    "scripts/agent_diff_check.py",
)


def changes(base: str | None) -> list[tuple[int, int, str]]:
    # Three dots diff against the merge base: only the branch's own work.
    revs = [f"{base}...HEAD"] if base else ["--cached"]
    out = subprocess.run(
        ["git", "diff", *revs, "--numstat", "--no-renames", "-z"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    rows = []
    for line in out.split("\0")[:-1]:  # -z ends every row with NUL
        added, deleted, path = line.split("\t", 2)
        if path in IGNORED:
            continue
        if added == "-":  # A binary file: keep the path, count no lines
            added = deleted = "0"
        rows.append((int(added), int(deleted), path))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="compare BASE...HEAD instead of the index")
    args = parser.parse_args()
    try:
        rows = changes(args.base)
    except subprocess.CalledProcessError as error:
        print(f"agent-diff-check: git diff failed: {error.stderr.strip()}")
        print("agent-diff-check: is the checkout shallow? Use fetch-depth: 0.")
        return 2
    problems = [
        f"protected path touched: {path}"
        for _, _, path in rows
        if path.startswith(PROTECTED)
    ]
    total = sum(a + d for a, d, _ in rows)
    if total > MAX_CHANGED_LINES:
        problems.append(f"diff changes {total} lines (limit {MAX_CHANGED_LINES})")
    for problem in problems:
        print(f"agent-diff-check: {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
