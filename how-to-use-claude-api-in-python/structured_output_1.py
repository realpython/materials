import anthropic
import json

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a Python coding assistant.",
    messages=[
        {
            "role": "user",
            "content": "Write a Python function that adds two numbers.",
        }
    ],
    output_config={
        "format": {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "function_name": {"type": "string"},
                    "code": {"type": "string"},
                    "explanation": {"type": "string"},
                },
                "required": ["function_name", "code", "explanation"],
                "additionalProperties": False,
            },
        }
    },
)

result = json.loads(response.content[0].text)

print("--- Approach 1: Hand-written JSON schema ---")
print(f"Function: {result['function_name']}")
print(f"\nCode:\n{result['code']}")
print(f"\nExplanation: {result['explanation']}")