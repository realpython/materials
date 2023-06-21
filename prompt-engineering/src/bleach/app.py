import os
from importlib import resources
from pathlib import Path
from typing import List

import openai
import tomllib
from dotenv import load_dotenv

# Authorization:
# Add your API key to the .env file as OPENAI_API_KEY
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the settings file
settings_path = resources.files(__package__) / "settings.toml"
with settings_path.open("rb") as settings_file:
    settings = tomllib.load(settings_file)

MODEL = settings["general"]["model"]
ROLE_PROMPT = settings["prompts"]["role_prompt"]
INSTRUCTIONS = settings["prompts"]["instructions"]


def sanitize(file: str, model: str = MODEL) -> str:
    """Assemble all prompts and send the API request."""
    content = _read_input_text(file)
    messages = _assemble_messages(content)

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
    )
    return response["choices"][0]["message"]["content"]


def _read_input_text(input_file: str) -> str:
    """Read the text content from a file."""
    input_file_path = Path(input_file)
    with input_file_path.open("r") as file:
        content = file.read()
    return content


def _assemble_messages(content: str) -> List[dict]:
    """Combine all messages into a well-formatted dictionary."""
    messages = [
        {"role": "system", "content": ROLE_PROMPT},
        {"role": "user", "content": f">>>\n{content}\n<<<\n\n"},
        {"role": "user", "content": INSTRUCTIONS},
    ]
    return messages
