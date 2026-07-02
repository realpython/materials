# Coordinating Teams of AI Agents with CrewAI in Python

Sample code for the Real Python tutorial
[CrewAI in Python: Coordinating Teams of AI Agents](https://realpython.com/crewai-python/).

## Requirements

- Python 3.10 to 3.13 (CrewAI does not support 3.14+)
- A free [Google AI Studio](https://aistudio.google.com/) API key for Gemini

## Setup

Create and activate a virtual environment, then install the dependencies:

```console
$ python -m venv venv
$ source venv/bin/activate     # On Windows: .\venv\Scripts\activate
$ python -m pip install -r requirements.txt
```

Set your Gemini API key as an environment variable:

```console
$ export GEMINI_API_KEY="your-gemini-api-key-here"
```

On Windows PowerShell:

```pscon
PS> $ENV:GEMINI_API_KEY = "your-gemini-api-key-here"
```

## Running the Examples

Each script corresponds to one section of the tutorial:

| File | Tutorial Section |
|------|------------------|
| `01_single_agent.py` | Get Started With CrewAI in Python |
| `02_research_and_writer_crew.py` | Build Your First Multi-Agent Team |
| `03_explicit_context.py` | Control Task Dependencies Explicitly |
| `04_agent_with_tools.py` | Expand Agent Capabilities With Tools |

Run any script with:

```console
$ python 01_single_agent.py
```

## Notes

- The `verbose=True` flag prints detailed agent reasoning logs — useful for
  learning, but noisy for production.
- If CrewAI complains about a missing `OPENAI_API_KEY` (e.g., when memory
  or certain tools are enabled), set it to any non-empty string to suppress
  the error.
- On first run, CrewAI may show a "Would you like to view your execution
  traces?" prompt that auto-dismisses after twenty seconds.
