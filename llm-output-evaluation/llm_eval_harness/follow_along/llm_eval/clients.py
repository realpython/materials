import json
import os
from pathlib import Path
from typing import Protocol, TypeVar

from openai import OpenAI, OpenAIError
from pydantic import BaseModel

SchemaT = TypeVar("SchemaT", bound=BaseModel)


class ModelClient(Protocol):
    """The model operations required by the harness.

    TODO (Step 3): declare generate_text() and generate_structured().
    """

    ...


class ReplayClient:
    """Replay checked-in generation and judgment responses."""

    def __init__(self, replay_dir: str | Path) -> None:
        path = Path(replay_dir) / "responses.json"
        self._responses = json.loads(path.read_text(encoding="utf-8"))

    def _lookup(self, section: str, request_id: str) -> object:
        try:
            return self._responses[section][request_id]
        except KeyError as exc:
            raise KeyError(f"no replay response for {request_id!r}") from exc

    def generate_text(
        self,
        request_id: str,
        model: str,
        instructions: str,
        input_text: str,
    ) -> str:
        del model, instructions, input_text
        response = self._lookup("text", request_id)
        if not isinstance(response, str):
            raise TypeError(f"replay response {request_id!r} is not text")
        return response

    def generate_structured(
        self,
        request_id: str,
        model: str,
        instructions: str,
        input_text: str,
        response_model: type[SchemaT],
    ) -> SchemaT:
        del model, instructions, input_text
        response = self._lookup("structured", request_id)
        return response_model.model_validate(response)


class OpenAIClient:
    """Use the OpenAI Responses API for live evaluation.

    TODO (Step 3): implement __init__(), _input(), generate_text(),
    and generate_structured().
    """

    def __init__(self, api_key: str | None = None) -> None:
        raise NotImplementedError("Build OpenAIClient in Step 3.")