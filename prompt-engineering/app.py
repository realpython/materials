import argparse
import os
import tomllib
from pathlib import Path

from openai import OpenAI

__all__ = ["get_chat_completion"]

# Authenticate
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load settings file
settings_path = Path("settings.toml")
with settings_path.open("rb") as settings_file:
    SETTINGS = tomllib.load(settings_file)


def parse_args() -> argparse.Namespace:
    """Parse command-line input."""
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=Path, help="Path to the input file")
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    file_content = args.file_path.read_text("utf-8")
    print(get_chat_completion(file_content))


def get_chat_completion(content: str) -> str:
    """Send a request to the /chat/completions endpoint."""
    response = client.chat.completions.create(
        model=SETTINGS["general"]["model"],
        messages=_assemble_chat_messages(content),
        temperature=SETTINGS["general"]["temperature"],
        seed=12345,  # Doesn't do anything for older models
    )
    return response.choices[0].message.content


def _assemble_chat_messages(content: str) -> list[dict]:
    """Combine all messages into a well-formatted list of dicts."""
    messages = [
        {"role": "system", "content": SETTINGS["prompts"]["role_prompt"]},
        {"role": "user", "content": SETTINGS["prompts"]["negative_example"]},
        {
            "role": "system",
            "content": SETTINGS["prompts"]["negative_reasoning"],
        },
        {
            "role": "assistant",
            "content": SETTINGS["prompts"]["negative_output"],
        },
        {"role": "user", "content": SETTINGS["prompts"]["positive_example"]},
        {
            "role": "system",
            "content": SETTINGS["prompts"]["positive_reasoning"],
        },
        {
            "role": "assistant",
            "content": SETTINGS["prompts"]["positive_output"],
        },
        {"role": "user", "content": f">>>>>\n{content}\n<<<<<"},
        {"role": "user", "content": SETTINGS["prompts"]["instruction_prompt"]},
    ]
    return messages


if __name__ == "__main__":
    main(parse_args())
