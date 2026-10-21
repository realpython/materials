# Build an AI Agent From Scratch in Python: The Agentic Loop

This folder contains sample code for the Real Python tutorial [Build an AI Agent From Scratch in Python: The Agentic Loop](https://realpython.com/agentic-loop/).

- `ai_agent.py`: the finished agent
- `source_code_step_1/` to `source_code_step_7/`: the script at the end of each step
- `habits/`: the sample project that the agent explores

The code uses Python 3.15. To run it, put your OpenAI API key in a `.env` file, then:

```console
$ export UV_ENV_FILE=.env
$ uv run --python 3.15 --with openai==3.31.0 ai_agent.py
```
