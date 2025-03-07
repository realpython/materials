# LangGraph: Build Stateful AI Agents in Python

This folder contains the source code for [LangGraph: Build Stateful AI Agents in Python](https://realpython.com/langgraph-python/)

## Setup

Create a new virtual environment, and run the following command to install LangGraph and the additional requirements for this project:

```console
(venv) $ python -m pip install -r requirements.txt
```

You'll use `langchain-openai` to interact with OpenAI LLMs, but keep in mind you can use any LLM provider you like with LangGraph and LangChain. You'll use [`pydantic`](https://realpython.com/python-pydantic/) to validate the information your agent parses from emails.

Before moving forward, if you choose to use OpenAI, make sure you're signed up for an OpenAI account and you have a valid [API key](https://openai.com/api/). You'll need to set the following [environment variable](https://en.wikipedia.org/wiki/Environment_variable) before running any examples in this tutorial:

```dotenv
OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>
```

## Usage

Once your environment is set up, you can run the final graph agent on an example input with the following code:

```python
from graphs.email_agent import email_agent_graph
from example_emails import EMAILS

escalation_criteria = """"There's an immediate risk of electrical,
water, or fire damage"""

message_with_criteria = f"""
The escalation criteria is: {escalation_criteria}

Here's the email:
{EMAILS[3]}
"""
message_3 = {"messages": [("human", message_with_criteria)]}
 
for chunk in email_agent_graph.stream(message_3, stream_mode="values"):
    chunk["messages"][-1].pretty_print()
```

See the tutorial for all the details on what's going on here.
