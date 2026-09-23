from typing import Literal, NamedTuple

from openai import OpenAI
from pydantic import BaseModel, ValidationError

MODEL = "gpt-5.6-luna"
client = OpenAI(timeout=60.0, max_retries=0)


class Decision(BaseModel):
    label: Literal["follow_up", "resolved", "unclear"]
    evidence: str


class Classification(NamedTuple):
    model: str
    decision: Decision


class ClassificationError(Exception):
    """The model didn't return a usable decision."""


def find_refusal(response):
    for item in response.output:
        for content in getattr(item, "content", []):
            if content.type == "refusal":
                return content.refusal
    return None


def classify(conversation, prompt):
    try:
        response = client.responses.parse(
            model=MODEL,
            instructions=prompt,
            input=conversation,
            text_format=Decision,
            reasoning={"effort": "low"},
            max_output_tokens=2048,
            store=False,
        )
    except ValidationError as error:
        raise ClassificationError(
            "truncated or unparsable JSON, so try raising max_output_tokens"
        ) from error
    if response.status == "incomplete":
        reason = getattr(response.incomplete_details, "reason", "unknown")
        raise ClassificationError(f"incomplete response: {reason}")
    if refusal := find_refusal(response):
        raise ClassificationError(f"refused: {refusal}")
    if response.status != "completed" or response.output_parsed is None:
        raise ClassificationError(f"no decision: status {response.status}")
    return Classification(response.model, response.output_parsed)
