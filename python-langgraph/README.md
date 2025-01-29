# LangGraph: Build Stateful AI Agents in Python

This repo contains the source code for [LangGraph: Build Stateful AI Agents in Python](https://realpython.com/langgraph-build-stateful-ai-agents-in-python/)

## Setup

LangGraph is available on [PyPI](https://pypi.org/), and you can install it with [pip](https://realpython.com/what-is-pip/). Open a terminal or command prompt, create a new virtual environment, and then run the following command to install LangGraph:

```console
(venv) $ python -m pip install langgraph
```

This command will install the latest version of LangGraph from PyPI onto your machine. To verify that the installation was successful, start a [Python REPL](https://realpython.com/python-repl/) and import LangGraph:

```pycon
>>> import langgraph
```

If the import runs without error, then you've successfully installed LangGraph. You'll also need a few more libraries for this tutorial:

```console
(venv) $ python -m pip install langchain-openai pydantic[email]
```

You'll use `langchain-openai` to interact with OpenAI LLMs, but keep in mind you can use any LLM provider you like with LangGraph and LangChain. You'll use [`pydantic`](https://realpython.com/python-pydantic/) to validate the information your agent parses from emails.

Before moving forward, if you choose to use OpenAI, make sure you're signed up for an OpenAI account and you have a valid [API key](https://openai.com/api/). You'll need to set the following [environment variable](https://en.wikipedia.org/wiki/Environment_variable) before running any examples in this tutorial:

```dotenv
OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>
```

Note that while LangGraph was made by the creators of LangChain, and the two libraries are highly compatible, it is possible to use LangGraph without LangChain. However, it's more common to use LangChain and LangGraph together, and you'll see throughout this tutorial how they compliment each other. 

With that, you've installed all the dependencies you'll need for this tutorial, and you're ready to create your LangGraph email processor. You'll start by going through an overview of LangChain chains and exploring LangGraph's core concept - the state graph.