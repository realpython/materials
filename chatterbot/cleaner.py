import re


def clean_corpus(chat_export_file):
    """Prepare a WhatsApp chat export for training with chatterbot."""
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_whatsapp_boilerplate(message_corpus)
    return cleaned_corpus


def remove_chat_metadata(chat_export_file):
    """Remove WhatsApp chat metadata.

    WhatsApp chat exports come with a boilerplate first intro line,
    as well as metadata about each message:

     date    time    username  message
    ---------------------------------------
    8/26/22, 17:47 - Jane Doe: Message text

    This function removes the first boilerplate line of a chat export
    as well as all the metadata up to the text of each message.

    Args:
        chat_export_file (str): The name of the chat export file

    Returns:
        tuple: The text of all messages in the conversation
    """
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # "8/26/22, 17:47"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # "Jane Doe"
    metadata_whitespace = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_whitespace

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
        cleaned_corpus = re.sub(pattern, "", content)
        return tuple(cleaned_corpus.split("\n")[1:])


def remove_whatsapp_boilerplate(message_collection):
    """Remove conversation-irrelevant text from chat export."""
    boilerplate = (
        "<Media omitted>",
        "<media omitted>",
    )
    return tuple((msg for msg in message_collection if msg not in boilerplate))
