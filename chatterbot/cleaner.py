import re


def clean_corpus(file_path):
    cleaned_corpus = remove_whatsapp_copypasta(remove_chat_metadata(file_path))
    return cleaned_corpus


def remove_chat_metadata(file_path):
    pattern = r"(\d+\/\d+\/\d+,\s\d+:\d+\s-\s)([\w\s]+)(:\s)"
    with open(file_path, "r") as corpus_file:
        content = corpus_file.read()
        cleaned_corpus = re.sub(pattern, "", content)
        return tuple(cleaned_corpus.split("\n"))


def remove_whatsapp_copypasta(message_collection):
    copypasta = (
        "Messages and calls are end-to-end encrypted. \
            No one outside of this chat, not even WhatsApp, \
            can read or listen to them. Tap to learn more."
        "<Media omitted>",
        "<media omitted>",
    )
    return tuple((msg for msg in message_collection if msg not in copypasta))
