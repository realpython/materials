import json
import os
from pathlib import Path
from typing import Protocol, TypeVar

from openai import OpenAI, OpenAIError
from pydantic import BaseModel

SchemaT = TypeVar("SchemaT", bound=BaseModel)


class ModelClient(Protocol):
    """The model operations required by the harness."""

    def generate_text(
        self,
        request_id: str,
        model: str,
        instructions: str,
        input_text: str,
    ) -> str:
        """Return ordinary application text."""
        ...

    def generate_structured(
        self,
        request_id: str,
        model: str,
        instructions: str,
        input_text: str,
        response_model: type[SchemaT],
    ) -> SchemaT:
        """Return output validated against a Pydantic model."""
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
    """Use the OpenAI Responses API for live evaluation."""

    def __init__(self, api_key: str | None = None) -> None:
        resolved_key = api_key or os.getenv("OPENAI_API_KEY")
        if not resolved_key:
            raise ValueError("OPENAI_API_KEY is required when --live is used")
        self._client = OpenAI(api_key=resolved_key)

    @staticmethod
    def _input(instructions: str, input_text: str) -> list[dict[str, str]]:
        return [
            {"role": "developer", "content": instructions},
            {"role": "user", "content": input_text},
        ]

    def generate_text(
        self,
        request_id: str,
        model: str,
        instructions: str,
        input_text: str,
    ) -> str:
        try:
            response = self._client.responses.create(
                model=model,
                input=self._input(instructions, input_text),
            )
        except OpenAIError as exc:
            raise RuntimeError(f"text request {request_id!r} failed") from exc
        if not response.output_text:
            raise RuntimeError(f"text request {request_id!r} returned no text")
        return response.output_text

    def generate_structured(
        self,
        request_id: str,
        model: str,
        instructions: str,
        input_text: str,
        response_model: type[SchemaT],
    ) -> SchemaT:
        try:
            response = self._client.responses.parse(
                model=model,
                input=self._input(instructions, input_text),
                text_format=response_model,
            )
        except OpenAIError:
            raise RuntimeError(f"structured request {request_id!r} failed")
        if response.output_parsed is None:
            raise RuntimeError(
                f"structured request {request_id!r} returned no parsed output"
            )
        return response_model.model_validate(response.output_parsed)


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    model = os.getenv("EVAL_GENERATOR_MODEL", "gpt-5.6-luna")
    client = OpenAIClient()
    reply = client.generate_text(
        request_id="smoke-test",
        model=model,
        instructions="You are a helpful assistant.",
        input_text="Reply with the single word: ready",
    )
    if reply.strip():
        print("OpenAI client is functional.")
