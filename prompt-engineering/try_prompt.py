from pathlib import Path

from classify import classify

conversation = """Customer: This blasted login never works!
Agent: Try the reset link.
Customer: That fixed it. I can log in now."""

prompt = Path("baseline.txt").read_text(encoding="utf-8")
model, decision = classify(conversation, prompt)
print(f"Answered by {model}")
print(decision.model_dump_json(indent=2))
