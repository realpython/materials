import pathlib
import re
import subprocess

PROMPT = """Fix this one failing test: {test}
Edit files under app/ only, never tests/. Leave the other tests alone."""
MAX_RUNS = 5
log = pathlib.Path("app.log")

for run in range(MAX_RUNS + 1):
    log.write_text("")  # Keep only this run's errors
    tests = subprocess.run(
        ["python", "-m", "pytest", "-q"], capture_output=True, text=True
    )
    if tests.returncode == 0:
        print(f"All tests pass after {run} agent run(s).", flush=True)
        break
    if run == MAX_RUNS:
        print(f"Gave up after {MAX_RUNS} runs.", flush=True)
        break
    failing = re.findall(r"^FAILED (\S+)", tests.stdout, re.M)
    lines = log.read_text().splitlines()
    error = lines[-1] if lines else "nothing logged"
    context = f"{tests.stdout}\n\napp.log shows: {error}"
    print(
        f"Run {run + 1}: {len(failing)} failing, handing over {failing[0]}",
        flush=True,
    )
    subprocess.run(
        [
            "claude",
            "-p",
            f"{PROMPT.format(test=failing[0])}\n\n{context}",
            "--permission-mode",
            "manual",
            "--allowedTools",
            "Read,Edit,Write",
        ],
        check=True,
    )
