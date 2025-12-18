from llama_index.core import SimpleDirectoryReader

reader = SimpleDirectoryReader(input_files=["./data/pep8.rst"])
documents = reader.load_data()

print(documents[0].text)
