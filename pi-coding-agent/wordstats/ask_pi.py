"""Run pi in JSON mode and print each tool call and the final answer."""

import json
import subprocess
import sys

MODEL = ["--model", "openai/gpt-5.4-mini", "--thinking", "off"]
if len(sys.argv) != 2:
    sys.exit("Usage: python ask_pi.py PROMPT")
cmd = ["pi", "--mode", "json", "--no-session", *MODEL, "-p", sys.argv[1]]
answer, failed = "", False
with subprocess.Popen(
    cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, encoding="utf-8"
) as proc:
    for line in proc.stdout:
        event = json.loads(line)
        if event["type"] == "tool_execution_start":
            print("tool:", event["toolName"])
        elif event["type"] == "agent_end":
            for msg in event["messages"]:
                if msg["role"] == "assistant":
                    texts = [part.get("text", "") for part in msg["content"]]
                    answer = "".join(texts) or msg.get("errorMessage", "")
                    failed = msg.get("stopReason") == "error"
        elif event["type"] == "agent_settled":
            print("answer:", answer)
sys.exit(1 if failed else proc.returncode)
