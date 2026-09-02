from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

Verdict = Literal["PASS", "FAIL", "REVIEW"]
ResultType = Literal["categorical", "ordinal"]


class StrictModel(BaseModel):
    """Reject unknown fields in checked-in evaluation artifacts."""

    model_config = ConfigDict(extra="forbid")


class Criterion(StrictModel):
    id: str
    display_name: str
    description: str
    result_type: ResultType
    oracle: Literal["code", "reference", "llm", "hybrid"]
    blocker: bool
    anchors: dict[str, str] = Field(default_factory=dict)
    scale: dict[str, str] = Field(default_factory=dict)
    pass_threshold: int | None = None
    require_response_quote: bool = True
    require_policy_quote: bool = False

    @model_validator(mode="after")
    def validate_scale(self) -> "Criterion":
        if self.result_type == "categorical":
            if set(self.anchors) != {"PASS", "FAIL", "REVIEW"}:
                raise ValueError("categorical criteria need three anchors")
            if self.scale or self.pass_threshold is not None:
                raise ValueError("categorical criteria cannot define a scale")
        else:
            scores = sorted(int(score) for score in self.scale)
            if scores != list(range(scores[0], scores[-1] + 1)):
                raise ValueError("ordinal scales must be contiguous")
            if self.pass_threshold not in scores:
                raise ValueError("pass_threshold must be on the scale")
            if self.anchors:
                raise ValueError("ordinal criteria use scale, not anchors")
        return self


class Rubric(StrictModel):
    schema_version: str
    id: str
    criteria: list[Criterion]

    @model_validator(mode="after")
    def validate_unique_ids(self) -> "Rubric":
        ids = [criterion.id for criterion in self.criteria]
        if len(ids) != len(set(ids)):
            raise ValueError("criterion IDs must be unique")
        return self


class ExpectedBehavior(StrictModel):
    decision: str
    required_facts: list[str]
    forbidden_patterns: list[str] = Field(default_factory=list)
    maximum_words: int = 90


class EvalCase(StrictModel):
    schema_version: str
    id: str
    split: Literal["dev", "release", "regression"]
    user_message: str
    policy: str
    expected: ExpectedBehavior
    criteria: list[str]
    tags: list[str]
    critical: bool = False


class CalibrationCase(StrictModel):
    id: str
    case_id: str
    criterion_id: str
    candidate_response: str
    human_labels: list[Verdict]
    adjudicated_label: Verdict
    critical: bool
    canary: bool = False


class CategoricalJudgment(StrictModel):
    kind: Literal["categorical"] = "categorical"
    criterion_id: str
    label: Verdict
    reason: str
    response_quote: str = ""
    policy_quote: str = ""


class OrdinalJudgment(StrictModel):
    kind: Literal["ordinal"] = "ordinal"
    criterion_id: str
    score: int
    reason: str
    response_quote: str = ""
    policy_quote: str = ""


Judgment = CategoricalJudgment | OrdinalJudgment


class JudgeResponse(StrictModel):
    results: list[Judgment]


class MetricResult(StrictModel):
    criterion_id: str
    result_type: ResultType
    verdict: Verdict
    score: int | None = None
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
