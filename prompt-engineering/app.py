import argparse
import os
import tomllib
from pathlib import Path

import openai

# Authenticate
openai.api_key = os.getenv("OPENAI_API_KEY")


class Settings(dict):
    """Handle loading and accessing application settings from file."""

    @classmethod
    def load(cls, path) -> "Settings":
        """Load TOML settings file and pass it to class constuctor."""
        with path.open("rb") as file:
            return cls(tomllib.load(file))

    def __init__(self, *args, **kwargs) -> None:
        """Add general settings and prompts as instance attributes."""
        super().__init__(*args, **kwargs)
        # Settings
        self.chat_models = self["general"]["chat_models"]
        self.model = self["general"]["model"]
        self.max_tokens = self["general"]["max_tokens"]
        self.temperature = self["general"]["temperature"]
        self.model_supports_chat_completions = self.model in self.chat_models
        # Prompts
        self.instruction_prompt = self["prompts"]["instruction_prompt"]
        self.role_prompt = self["prompts"]["role_prompt"]
        self.positive_example = self["prompts"]["positive_example"]
        self.positive_reasoning = self["prompts"]["positive_reasoning"]
        self.positive_output = self["prompts"]["positive_output"]
        self.negative_example = self["prompts"]["negative_example"]
        self.negative_reasoning = self["prompts"]["negative_reasoning"]
        self.negative_output = self["prompts"]["negative_output"]


def parse_args() -> argparse.Namespace:
    """Parse command-line input."""
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path, help="Path to the input file")
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    file_content = args.file_path.read_text("utf-8")
    settings = Settings.load(Path("settings.toml"))
    if settings.model_supports_chat_completions:
        print(get_chat_completion(file_content, settings))
    else:
        print(get_completion(file_content, settings))


def get_completion(content: str, settings: Settings) -> str:
    """Send a request to the /completions endpoint."""
    response = openai.Completion.create(
        model=settings.model,
        prompt=assemble_prompt(content, settings),
        max_tokens=settings.max_tokens,
        temperature=settings.temperature,
    )
    return response["choices"][0]["text"]


def get_chat_completion(content: str, settings: Settings) -> str:
    """Send a request to the /chat/completions endpoint."""
    response = openai.ChatCompletion.create(
        model=settings.model,
        messages=assemble_chat_messages(content, settings),
        temperature=settings.temperature,
    )
    return response["choices"][0]["message"]["content"]


def assemble_prompt(content: str, settings: Settings) -> str:
    """Combine all text input into a single prompt."""
    return f">>>>>\n{content}\n<<<<<\n\n" + settings.instruction_prompt


def assemble_chat_messages(content: str, settings: Settings) -> list[dict]:
    """Combine all messages into a well-formatted dictionary."""
    return [
        {"role": "system", "content": settings.role_prompt},
        {"role": "user", "content": settings.negative_example},
        {"role": "system", "content": settings.negative_reasoning},
        {"role": "assistant", "content": settings.negative_output},
        {"role": "user", "content": settings.positive_example},
        {"role": "system", "content": settings.positive_reasoning},
        {"role": "assistant", "content": settings.positive_output},
        {"role": "user", "content": f">>>>>\n{content}\n<<<<<"},
        {"role": "user", "content": settings.instruction_prompt},
    ]


if __name__ == "__main__":
    main(parse_args())
