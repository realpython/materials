import re


def clean_corpus(chat_export_file):
    """Prepare a WhatsApp chat export for training with chatterbot."""
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_whatsapp_boilerplate(message_corpus)
    return cleaned_corpus


def remove_chat_metadata(chat_export_file):
    """Remove WhatsApp chat metadata (date, time, username, and whitespace)."""
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # "8/26/19, 17:47"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # "Jane Doe"
    metadata_whitespace = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_whitespace

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
        cleaned_corpus = re.sub(pattern, "", content)
        return tuple(cleaned_corpus.split("\n"))


def remove_whatsapp_boilerplate(message_collection):
    """Remove conversation-irrelevant text from chat export."""
    whatsapp_intro_line = (
        "Messages and calls are end-to-end encrypted. "
        "No one outside of this chat, not even WhatsApp, "
        "can read or listen to them. Tap to learn more."
    )
    boilerplate = (
        whatsapp_intro_line,
        "<Media omitted>",
        "<media omitted>",
    )
    breakpoint()
    return tuple((msg for msg in message_collection if msg not in boilerplate))
