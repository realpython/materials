"""Records for test cases, agent runs, and evaluation results."""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict

Verdict = Literal["PASS", "FAIL", "REVIEW"]
ResultType = Literal["categorical", "ordinal"]


class StrictModel(BaseModel):
    """Reject unknown fields in checked-in evaluation artifacts."""

    model_config = ConfigDict(extra="forbid")


class ExpectedBehavior(StrictModel):
    required_patterns: list[str]
    forbidden_patterns: list[str]
    tools: list[str]
    match: Literal["strict", "in_order", "unordered"]
    max_tool_calls: int
    arguments: dict[str, dict[str, str]]


class AgentCase(StrictModel):
    schema_version: str
    id: str
    user_message: str
    expected: ExpectedBehavior
    tags: list[str]
    critical: bool


class ToolCall(StrictModel):
    name: str
    arguments: dict[str, Any]
    result: str


class AgentTrace(StrictModel):
    question: str
    steps: list[ToolCall]
    answer: str
    turns: int


class AgentRun(StrictModel):
    case_id: str
    prompt_id: str
    trial: int
    trace: AgentTrace


class MetricResult(StrictModel):
    criterion_id: str
    result_type: ResultType
    verdict: Verdict
    score: float | None = None
    source: Literal["code", "reference", "llm_judge"]
    reason: str
    response_quote: str = ""
    policy_quote: str = ""


class Trial(StrictModel):
    case_id: str
    prompt_id: str
    critical: bool
    response: str
    metrics: list[MetricResult]
