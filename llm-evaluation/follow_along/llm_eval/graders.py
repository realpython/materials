import re

from .clients import ModelClient
from .models import (
    Criterion,
    EvalCase,
    MetricResult,
)

# TODO (Step 5): add JUDGE_SYSTEM_INSTRUCTIONS here.

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


# TODO (Step 4): add word_count(), deterministic_grade(), and
# pending_result() above evaluate_response().

# TODO (Step 5): add normalized(), unwrap_excerpt(), quote_is_present(),
# and review_result() before grade_with_judge().


def grade_with_judge(
    client: ModelClient,
    request_id: str,
    model: str,
    case: EvalCase,
    criteria: list[Criterion],
    response: str,
) -> list[MetricResult]:
    """Grade a response with an LLM judge.

    TODO (Step 5): build the judge request, call the client, and validate
    the returned judgments against the rubric and the source text.
    """
    raise NotImplementedError("Build grade_with_judge() in Step 5.")


def evaluate_response(
    client: ModelClient,
    request_id: str,
    model: str,
    case: EvalCase,
    criteria: dict[str, Criterion],
    response: str,
    deterministic_only: bool = False,
) -> list[MetricResult]:
    """Apply the oracle hierarchy to one response.

    TODO (Step 4): run the deterministic graders and collect delegated
    criteria. TODO (Step 5): send the delegated criteria to the judge.
    """
    raise NotImplementedError("Build evaluate_response() in Step 4.")
