import asyncio
from pathlib import Path

from llama_index.core import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)

# Define the storage directory
BASE_DIR = Path(__file__).resolve().parent
PERSIST_DIR = BASE_DIR / "storage"
DATA_FILE = BASE_DIR / "data" / "pep8.rst"


def get_index(persist_dir=PERSIST_DIR, data_file=DATA_FILE):
    if persist_dir.exists():
        storage_context = StorageContext.from_defaults(
            persist_dir=str(persist_dir),
        )
        index = load_index_from_storage(storage_context)
        print("Index loaded from storage...")
    else:
        reader = SimpleDirectoryReader(input_files=[str(data_file)])
        documents = reader.load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=str(persist_dir))
        print("Index created and persisted to storage...")

    return index


async def main():
    index = get_index()
    query_engine = index.as_query_engine()

    queries = [
        "What is this document about?",
        "Summarize the naming conventions in Python.",
    ]

    # Run queries asynchronously
    tasks = [query_engine.aquery(query) for query in queries]
    responses = await asyncio.gather(*tasks)

    # Print responses
    for i, (query, response) in enumerate(zip(queries, responses), 1):
        print(f"\nQuery {i}: {query}")
        print(f"Response: {response}\n")
        print("-" * 80)


if __name__ == "__main__":
    asyncio.run(main())
