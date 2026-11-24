"""Drive pi over RPC: two prompts in one session, then inspect the session."""

import json
import subprocess

MODEL = ["--model", "openai/gpt-5.4-mini", "--thinking", "off"]
cmd = ["pi", "--mode", "rpc", "--no-session", *MODEL]
with subprocess.Popen(
    cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8"
) as pi:

    def send(command):
        pi.stdin.write(json.dumps(command) + "\n")
        pi.stdin.flush()
        for line in pi.stdout:
            event = json.loads(line)
            if event["type"] == "response":
                print(event["command"], "->", json.dumps(event["data"])[:100])
            if event["type"] == "agent_settled" or (
                event["type"] == "response" and command["type"] != "prompt"
            ):
                return event

    send({"type": "prompt", "message": "Remember the number 42."})
    send(
        {"type": "prompt", "message": "What number did I ask you to remember?"}
    )
    send({"type": "get_last_assistant_text"})
    send({"type": "get_session_stats"})
    pi.stdin.close()
