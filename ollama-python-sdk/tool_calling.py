import math

from ollama import chat


# Define a tool as a Python function
def square_root(number: float) -> float:
    """Calculate the square root of a number.

    Args:
        number: The number to calculate the square root for.

    Returns:
        The square root of the number.
    """
    return math.sqrt(number)


messages = [
    {
        "role": "user",
        "content": "What is the square root of 36?",
    }
]

response = chat(
    model="llama3.2:latest",
    messages=messages,
    tools=[square_root],  # Pass the tools along with the prompt
)

# Append the response for context
messages.append(response.message)

if response.message.tool_calls:
    tool = response.message.tool_calls[0]
    # Call the tool
    result = square_root(float(tool.function.arguments["number"]))

    # Append the tool result
    messages.append(
        {
            "role": "tool",
            "tool_name": tool.function.name,
            "content": str(result),
        }
    )

    # Obtain the final answer
    final_response = chat(model="llama3.2:latest", messages=messages)
    print(final_response.message.content)
