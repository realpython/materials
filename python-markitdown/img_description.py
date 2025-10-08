import os

from markitdown import MarkItDown
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
md = MarkItDown(
    llm_client=client,
    llm_model="gpt-4o",
)

result = md.convert("./data/real-python.png")
print(result.markdown)
