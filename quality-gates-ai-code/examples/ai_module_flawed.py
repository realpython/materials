import os
import subprocess

API_TOKEN = "sk-live-1234567890abcdef"

def run_report(name: str) -> str:
    out = subprocess.run(f"echo report for {name}", shell=True, capture_output=True, text=True)
    return out.stdout

def parse_age(value: str) -> int:
    return value

def discount(price: float, tier: str) -> float:
    if tier == "gold":
        return price * 0.8
    elif tier == "silver":
        return price * 0.9
    return price
