# AI Agent Evaluation: Build an Eval Harness in Python

This folder contains the sample code for the Real Python tutorial
[AI Agent Evaluation: Build an Eval Harness in Python](https://realpython.com/agent-evaluation/).

It holds a small helpdesk agent for internal Python packages (`agent.py`,
`tools.py`) and an eval harness (`agent_evals.py`, `models.py`) that scores
each run's final answer, trajectory, and tool selection.

- The top-level folder holds the finished project.
- The `follow_along/` folder holds the starter project. The functions you
  write in the tutorial are stubs there.

## Setup

```console
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ python -m pip install -r requirements.txt
(.venv) $ export OPENAI_API_KEY="sk-..."
```

The agent uses `gpt-5.4-mini-2026-03-17`. Set the `AGENT_MODEL` environment
variable to try another model.

## Usage

```console
(.venv) $ python agent_evals.py run --prompt prompts/helpdesk_v1.txt
(.venv) $ python agent_evals.py report runs/helpdesk_v1.jsonl
(.venv) $ python agent_evals.py compare \
    runs/helpdesk_v1.jsonl runs/helpdesk_v2_docs_first.jsonl
```

The optional DeepEval example needs its own requirements file:

```console
(.venv) $ python -m pip install -r requirements-deepeval.txt
(.venv) $ python deepeval_tools.py
```
