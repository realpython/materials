import re


def clean_corpus(chat_export_file):
    """Prepare a WhatsApp chat export for training with chatterbot."""
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_whatsapp_boilerplate(message_corpus)
    return cleaned_corpus


def remove_chat_metadata(chat_export_file):
    """Remove WhatsApp chat metadata.

    WhatsApp chat exports come with metadata about each message:

     date    time    username  message
    ---------------------------------------
    8/26/22, 17:47 - Jane Doe: Message text

    This function removes all the metadata up to the text of each message.

    Args:
        chat_export_file (str): The name of the chat export file

    Returns:
        tuple: The text of each message in the conversation
    """
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # "8/26/22, 17:47"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # "Jane Doe"
    metadata_whitespace = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_whitespace

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
        cleaned_corpus = re.sub(pattern, "", content)
        return tuple(cleaned_corpus.split("\n"))


def remove_whatsapp_boilerplate(message_collection):
    """Remove conversation-irrelevant text from chat export.

    WhatsApp chat exports come with a boilerplate intro line.
    Text exports also replace media messages with text that isn't
    relevant for the conversation. This function removes both.

    Args:
        message_collection (tuple): Message texts

    Returns:
        tuple: Messages without WhatsApp boilerplate
    """
    messages = message_collection[1:]

    boilerplate = (
        "<Media omitted>",
        "<media omitted>",
    )
    return tuple((msg for msg in messages if msg not in boilerplate))
