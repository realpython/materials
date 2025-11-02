from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")

result = md.convert("./data/real-python.png")
print(result.markdown)
