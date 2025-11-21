from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI

reader = SimpleDirectoryReader(input_files=["./data/pep8.rst"])
documents = reader.load_data()
index = VectorStoreIndex.from_documents(documents)

llm = OpenAI(model="gpt-5.1")
query_engine = index.as_query_engine(llm=llm)

response = query_engine.query("Summarize the import rules.")
print(response)
