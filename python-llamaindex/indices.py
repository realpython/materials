import asyncio
import logging

from llama_index.core import (
    SimpleDirectoryReader,
    SummaryIndex,
    TreeIndex,
    VectorStoreIndex,
)
from llama_index.llms.openai import OpenAI

# Disable logging messages
logging.getLogger("llama_index").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

reader = SimpleDirectoryReader(input_files=["./data/pep8.rst"])
documents = reader.load_data()
llm = OpenAI(model="gpt-4o-mini")

# Different index types
vector_index = VectorStoreIndex.from_documents(documents)
summary_index = SummaryIndex.from_documents(documents)
tree_index = TreeIndex.from_documents(documents)

# Create query engines
vector_qe = vector_index.as_query_engine(llm=llm)
summary_qe = summary_index.as_query_engine(llm=llm)
tree_qe = tree_index.as_query_engine(llm=llm)


async def main():
    query = "What is this document about?"

    print("Vector Index:")
    response = await vector_qe.aquery(query)
    print(response, "\n")

    print("Summary Index:")
    response = await summary_qe.aquery(query)
    print(response, "\n")

    print("Tree Index:")
    response = await tree_qe.aquery(query)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
