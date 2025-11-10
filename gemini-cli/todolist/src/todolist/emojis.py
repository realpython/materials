import os
import typing
from collections.abc import Sequence
from functools import cache

if typing.TYPE_CHECKING:
    from openai import OpenAI

MODEL = "gpt-4o-mini"
TEMPERATURE = 0.3
MAX_TOKENS = 10

SYSTEM_PROMPT = (
    "You are an emoji expert. When given a phrase, you respond with only "
    "a single emoji that best matches it. Never include explanations or "
    "multiple emojis."
)

BATCH_USER_PROMPT = (
    "Given the list of PHRASES below (each on a separate line), return ONLY "
    "a list of emojis (one per line) that best represents each phrase. "
    "Return ONLY the emoji characters themselves in the same order, with no "
    "explanation or additional text. One emoji per line."
)


def has_emoji_support() -> bool:
    if "NO_EMOJI" in os.environ:
        return False
    return os.environ.get("OPENAI_API_KEY") is not None


def find_matching_emojis(phrases: Sequence[str]) -> tuple[str | None, ...]:
    if not phrases:
        return tuple()

    if client := _get_client():
        phrases_text = "\n".join(
            f"{i + 1}. {phrase}" for i, phrase in enumerate(phrases)
        )
        user_prompt = BATCH_USER_PROMPT + f"\n\nPHRASES:\n{phrases_text}"
        try:
            response = client.chat.completions.create(
                model=MODEL,
                max_tokens=MAX_TOKENS * len(phrases),
                temperature=TEMPERATURE,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            )
            emojis = response.choices[0].message.content.strip().split("\n")
            result = []
            for i in range(len(phrases)):
                if i < len(emojis):
                    emoji = emojis[i].strip()
                    if emoji and emoji[0].isdigit():
                        emoji = emoji.split(".", 1)[-1].strip()
                    result.append(emoji[0] if emoji else None)
                else:
                    result.append(None)
            return tuple(result)
        except Exception:
            return (None,) * len(phrases)
    else:
        return (None,) * len(phrases)


@cache
def _get_client() -> OpenAI | None:
    from openai import OpenAI

    return OpenAI() if has_emoji_support() else None
