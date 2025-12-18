# MCP Client

A minimal client for testing Model Context Protocol (MCP) servers, featuring AI integration.

## Features

- **MCP server integration**: Connect to any MCP server
- **Server introspection**: List available tools, prompts, and resources with the `--members` option
- **TUI AI-powered chat**: Interactive chat with AI-powered tool execution using the `--chat` option

## Installation

1. Download the sample code

2. Install dependencies:
```console
$ uv sync
```

3. Set up your OpenAI API key:
```console
$ export OPENAI_API_KEY="your-openai-api-key"
```

## Usage

### List Server Members

Inspect what tools, prompts, and resources are available on an MCP server:

```console
$ uv run python -m mcp_client /path/to/mcp_server.py --members
```

This command will display the following:

- Tools and their descriptions
- Prompts and their purposes
- Resources and their types

### Interactive Chat Mode

Start an interactive chat session using the MCP server tools:

```console
$ uv run python -m mcp_client <path/to/mcp/server.py> --chat
```

- Example - Ask questions and get AI-powered responses:
```console
$ uv run python -m mcp_client mcp_server/mcp_server.py --chat

MCP Client Started!
Type your queries or 'quit' to exit.

You: Greet Pythonista

Assistant: [Used echo({'message': "Hello, Pythonista! 🐍 How's your coding journey going today?"})]
Hello, Pythonista! 🐍 How's your coding journey going today?

You:
```

- The AI will automatically use available MCP tools when needed
- Type `quit` to exit

## Example MCP Server

The project includes, `mcp_server.py`, which is a minimal MCP server that provides:

- A sample tool that says hello
- Sample prompts and resources

You can use this server to test the client's functionalities.

## Requirements

- Python >= 3.13
- The MCP Python SDK and OpenAI Python SDK
- An OpenAI API key
- An MCP server to connect to
