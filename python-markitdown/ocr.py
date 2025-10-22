from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(
    llm_client=client,
    llm_model="gpt-4o",
    llm_prompt="Extract text from image with OCR and return Markdown.",
)

result = md.convert("./data/zen-of-python.png")
print(result.markdown)
