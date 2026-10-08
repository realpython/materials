import sys
from pathlib import Path

from cases import DEV_CASES
from classify import MODEL, ClassificationError, classify
from openai import APIError

prompt = Path(sys.argv[1]).read_text(encoding="utf-8")
matches = 0
quotes = 0
failures = 0
answered_by = set()

print(f"Model requested: {MODEL}; prompt: {sys.argv[1]}")
for name, expected, conversation in DEV_CASES:
    try:
        model, decision = classify(conversation, prompt)
    except (APIError, ClassificationError) as error:
        failures += 1
        print(f"{name}: request failed: {error}")
        continue
    answered_by.add(model)
    matched = decision.label == expected
    quoted = bool(decision.evidence) and decision.evidence in conversation
    matches += matched
    quotes += quoted
    print(f"{name}: expected={expected}, got={decision.label}")
    print(f"  Exact quote: {quoted}; evidence: {decision.evidence!r}")

print(f"Labels: {matches}/{len(DEV_CASES)}")
print(f"Exact quotes: {quotes}/{len(DEV_CASES)}; failures: {failures}")
print(f"Answered by: {', '.join(sorted(answered_by)) or 'nothing'}")
