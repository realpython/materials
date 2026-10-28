import subprocess
import uuid

IMAGE = "python:3.15-slim"
RUN = ["docker", "run"]
REMOVE = ["docker", "rm", "--force"]
FLAGS = [
    "--network=none",
    "--read-only",
    "--ipc=none",
    "--cap-drop=ALL",
    "--security-opt=no-new-privileges",
    "--user=65534:65534",
    "--memory=128m",
    "--memory-swap=128m",
    "--cpus=1",
    "--pids-limit=64",
    "--log-driver=none",
]


def run_untrusted(code, timeout=5):
    name = f"sandbox-{uuid.uuid4().hex[:12]}"
    command = [*RUN, "--rm", "--interactive", f"--name={name}", *FLAGS]
    try:
        result = subprocess.run(
            [*command, IMAGE, "python", "-"],
            input=code,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        cleanup = subprocess.run(
            [*REMOVE, name], capture_output=True, text=True, timeout=30
        )
        if cleanup.returncode != 0:
            if "no such container" not in cleanup.stderr.lower():
                raise RuntimeError(f"Couldn't remove {name}: {cleanup.stderr}")
        return {"exit_code": None, "stdout": "", "stderr": "timed out"}
    return {
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
