import os
import requests

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

api_key = os.getenv("OPENROUTER_API_KEY")

def make_request_with_fallback(models_list, messages):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {"models": models_list, "messages": messages}

    return requests.post(OPENROUTER_API_URL, headers=headers, json=payload)

response = make_request_with_fallback(
    models_list=[
        "openai/gpt-5",
        "openai/gpt-3.5-turbo",
        "openai/gpt-3.5-turbo-16k"
    ],
    messages=[{"role": "user", "content": "What is the capital of France?"}]
)

data = response.json()
if model := data.get('model'):
    print(f"Model: {model} by {data['provider']}")
    print(f"Response: {data['choices'][0]['message']['content']}")
else:
    print("No model found in the response.")
    print(f"Response: {data}")