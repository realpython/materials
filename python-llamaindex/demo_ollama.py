from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

reader = SimpleDirectoryReader(input_files=["./data/pep8.rst"])
documents = reader.load_data()

embed_model = OllamaEmbedding(
    model_name="embeddinggemma",
    request_timeout=60.0,  # For low-performance hardware
    context_window=8000,  # For reducing memory usage
)
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

llm = Ollama(model="llama3.2")
query_engine = index.as_query_engine(llm=llm)

response = query_engine.query("What is this document about?")
print(response)
