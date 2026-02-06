import os
import requests

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

api_key = os.getenv("OPENROUTER_API_KEY")


def make_request(model, messages, provider_config=None):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {"model": model, "messages": messages}
    if provider_config:
        payload["provider"] = provider_config

    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


data = make_request(
    model="meta-llama/llama-3.1-70b-instruct",
    messages=[{"role": "user", "content": "Explain AI in one sentence."}],
    provider_config={"sort": "price"},
)

if model := data.get("model"):
    print(f"Model: {model} by {data['provider']}")
    print(f"Response: {data['choices'][0]['message']['content']}")
else:
    print("No model found in the response.")
    print(f"Response: {data}")
