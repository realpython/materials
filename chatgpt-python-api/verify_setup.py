from openai import OpenAI

client = OpenAI()
print("OpenAI client created successfully!")
print(f"Using API key: {client.api_key[:8]}...")
