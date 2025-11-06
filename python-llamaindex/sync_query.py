import logging
from pathlib import Path

from llama_index.core import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)

# Disable logging messages
logging.getLogger("llama_index").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

# Define the storage directory
PERSIST_DIR = "./storage"


def get_index(persist_dir=PERSIST_DIR):
    if Path(persist_dir).exists():
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
        print("Index loaded from storage...")
    else:
        reader = SimpleDirectoryReader(input_files=["./data/pep8.rst"])
        documents = reader.load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=persist_dir)
        print("Index created and persisted to storage...")

    return index


def main():
    index = get_index()
    query_engine = index.as_query_engine()
    response = query_engine.query("What is this document about?")
    print(response)


if __name__ == "__main__":
    main()
