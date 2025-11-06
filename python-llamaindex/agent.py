import asyncio

import requests
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.openai import OpenAI


def get_breed_info(breed_name):
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    response.raise_for_status()
    for breed in response.json():
        if breed["name"] == breed_name:
            return breed
    return None


workflow = AgentWorkflow.from_tools_or_functions(
    tools_or_functions=[get_breed_info],
    llm=OpenAI(model="gpt-4o-mini"),
    system_prompt="You are an agent that can provide information about cat breeds.",
)


async def main():
    response = await workflow.run(
        user_msg="Can you describe the temperament of Siamese cats?"
    )
    print(response)


if __name__ == "__main__":

    asyncio.run(main())
