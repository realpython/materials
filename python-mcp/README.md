# Python MCP: Connect Your LLM With the World

This repo contains the source code for [Python MCP: Connect Your LLM With the World](https://realpython.com/python-mcp-connect-your-llm-with-world/)

## Setup

Create a new virtual environment, and run the following command to install Python MCP and the additional requirements for this project:

```console
(venv) $ python -m pip install "mcp[cli]"
```

You'll use [`pytest-asyncio`](https://realpython.com/pytest-python-testing/) to test your MCP server. With that, you've installed all the Python dependencies you'll need for this tutorial, and you're ready to dive into MCP!

## Usage

Once your environment is set up, you can run the MCP server with the following command:

```console
(venv) $ python main.py
```

In `test/test_server.py`, you'll also want to change `SERVER_PATH` to the local path to your `main.py` file. See the tutorial for all the details on what's going on here, along with how to connect your server to Cursor's MCP client.