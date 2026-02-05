import os
import requests

OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"

api_key = os.getenv("OPENROUTER_API_KEY")

headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(OPENROUTER_MODELS_URL, headers=headers)
data = response.json()

models = data.get("data", [])
print(f"Success! Found {len(models)} models via OpenRouter.")
print(f"Examples: {', '.join(m['id'] for m in models[:5])}")