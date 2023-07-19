import os
import sys
import tomllib
from pathlib import Path
from typing import List

import openai

# Authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")


def main() -> str:
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "training.txt"
    settings = _load_settings()
    if settings["general"]["model"] in settings["general"]["chat_models"]:
        return request_response(file_path)
    return request_completion(file_path)


def request_completion(file: str) -> str:
    """Assemble all text into a prompt and send a /completion API request."""
    settings = _load_settings()
    content = _read_input_text(file)
    prompt = _assemble_prompt(content, settings)

    response = openai.Completion.create(
        model=settings["general"]["model"],
        prompt=prompt,
        max_tokens=settings["general"]["max_tokens"],
        temperature=settings["general"]["temperature"],
    )
    return response["choices"][0]["text"]


def request_response(file: str) -> str:
    """Assemble all text into a prompt and send a /chat API request."""
    settings = _load_settings()
    content = _read_input_text(file)
    messages = _assemble_messages(content, settings)

    response = openai.ChatCompletion.create(
        model=settings["general"]["model"],
        messages=messages,
        # max_tokens defaults to inf
        temperature=settings["general"]["temperature"],
    )
    return response["choices"][0]["message"]["content"]


def _load_settings() -> dict:
    """Load the settings file."""
    settings_path = Path.cwd() / "settings.toml"
    with settings_path.open("rb") as settings_file:
        settings = tomllib.load(settings_file)
    return settings


def _read_input_text(input_file: str) -> str:
    """Read the text content from a file."""
    input_file_path = Path(input_file)
    with input_file_path.open("r") as file:
        content = file.read()
    return content


def _assemble_prompt(content: str, settings: dict) -> str:
    """Combine all messages into a single prompt."""
    prompt = (
        f">>>>>\n{content}\n<<<<<\n\n" + settings["prompts"]["instructions"]
    )
    return prompt


def _assemble_messages(content: str, settings: dict) -> List[dict]:
    """Combine all messages into a well-formatted dictionary."""
    messages = [
        {"role": "system", "content": settings["prompts"]["role_prompt"]},
        {"role": "user", "content": f">>>>>\n{content}\n<<<<<\n\n"},
        {"role": "user", "content": settings["prompts"]["instructions"]},
    ]
    return messages


if __name__ == "__main__":
    print(main())
