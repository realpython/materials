"""
Demonstrate the utility of CLAUDE.md
"""

import boto3
from botocore.config import Config

config = Config(
    connect_timeout=15,
    read_timeout=3600,
    retries={"max_attempts": 4},
)

bedrock_client = boto3.client("bedrock-runtime", config=config)

MODEL_ID = "amazon.nova-premier-v1:0"
MAX_TOKENS = 100
TEMPERATURE = 0.1

SYSTEM_PROMPT = """You are a helpful, harmless assistant.
Your task is to assist customers with any questions they may have.
"""


def query_llm(prompt: str) -> str:
    system = [
        {"text": SYSTEM_PROMPT},
    ]

    messages = [{"role": "user", "content": [{"text": prompt}]}]
    inf_params = {"maxTokens": MAX_TOKENS, "temperature": TEMPERATURE}

    response = bedrock_client.converse(
        modelId=MODEL_ID,
        system=system,
        messages=messages,
        inferenceConfig=inf_params,
    )

    response_text = response["output"]["message"]["content"][0]["text"]
    return response_text


if __name__ == "__main__":
    query = input("Ask a question!\n>")
    response = query_llm(query)
    print(response)
