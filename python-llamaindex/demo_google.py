from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI

reader = SimpleDirectoryReader(input_files=["./data/pep8.rst"])
documents = reader.load_data()

embed_model = GoogleGenAIEmbedding(model="models/embedding-gecko-001")
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

llm = GoogleGenAI(model="gemini-2.5-flash")
query_engine = index.as_query_engine(llm=llm)

response = query_engine.query("What is this document about?")
print(response)
