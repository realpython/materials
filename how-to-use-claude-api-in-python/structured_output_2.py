import anthropic

from pydantic import BaseModel


class FunctionDescription(BaseModel):
    function_name: str
    code: str
    explanation: str

client = anthropic.Anthropic()

response = client.messages.parse(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a Python coding assistant.",
    messages=[
        {
            "role": "user",
            "content": "Write a Python function that adds two numbers.",
        }
    ],
    output_format=FunctionDescription,
)

result = response.parsed_output

print("--- Approach 2: Pydantic + client.messages.parse() ---")
print(f"Function: {result.function_name}")
print(f"\nCode:\n{result.code}")
print(f"\nExplanation: {result.explanation}")
