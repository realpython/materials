import re

# TODO (Step 5): JUDGE_SYSTEM_INSTRUCTIONS

SENSITIVE_PATTERNS = {
    "payment card": re.compile(r"(?<!\d)(?:\d[ -]?){13,19}(?!\d)"),
    "password": re.compile(r"\bpassword\s*(?:is|:)\s*\S+", re.IGNORECASE),
    "API key": re.compile(r"\b(?:sk|key)[-_][A-Za-z0-9_-]{16,}\b"),
}

CLOSING_QUOTES = {
    '"': '"',
    "'": "'",
    "\N{LEFT DOUBLE QUOTATION MARK}": "\N{RIGHT DOUBLE QUOTATION MARK}",
    "\N{LEFT SINGLE QUOTATION MARK}": "\N{RIGHT SINGLE QUOTATION MARK}",
}

# TODO (Step 4): Determnistic checks

# TODO (Step 5): Add judge helper functions

# TODO (Step 5): Add grade_with_judge()

# TODO (Step 4): evaluate_response()
