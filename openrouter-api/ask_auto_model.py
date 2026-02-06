import os
import requests

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
payload = {
    "model": "openrouter/auto",
    "messages": [{"role": "user", "content": "Say hello in one sentence."}],
}
response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
data = response.json()

print(f"Model: {data.get('model')}")
print(f"Response: {data['choices'][0]['message']['content']}")
