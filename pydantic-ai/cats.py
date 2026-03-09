import requests
from pydantic_ai import Agent

agent = Agent(
    "google-gla:gemini-2.5-flash",
    instructions="Help users with cat breeds. Be concise.",
)


@agent.tool_plain
def find_breed_info(breed_name: str) -> dict:
    """Find information about a cat breed."""
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    response.raise_for_status()
    json_response = response.json()
    for breed in json_response:
        if breed["name"] == breed_name:
            return breed
    return {"error": "Breed not found"}


result = agent.run_sync("Tell me about the Siamese cats.")
print(result.output)
