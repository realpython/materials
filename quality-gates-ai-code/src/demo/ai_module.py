import os
import subprocess  # nosec B404
import sys


def run_report(name: str) -> str:
    out = subprocess.run(  # noqa: S603  # nosec B603
        [sys.executable, "-c", "import sys; print('report for', sys.argv[1])", name],
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout


def parse_age(value: str) -> int:
    return int(value)


def discount(price: float, tier: str) -> float:
    if tier == "gold":
        return price * 0.8
    if tier == "silver":
        return price * 0.9
    return price


def api_token() -> str:
    return os.environ["API_TOKEN"]
