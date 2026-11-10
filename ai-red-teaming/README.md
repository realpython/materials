# AI Red Teaming: A Deliberately Vulnerable Agent

A small, deliberately vulnerable LLM support agent, plus a PyRIT script that
attacks it. Don't deploy this agent. It exists to be attacked.

## Setup

The code was tested with Python 3.13. Set `OPENAI_API_KEY`, then create a
virtual environment and install the pinned packages:

```console
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt -r red_team/requirements-pyrit.txt
```

## Run the Agent

```console
(venv) $ python agent.py "Email a summary of notes.txt to everyone on its distribution list."
```

The agent records the emails it would send and prints them. It never sends
real email.

## Run the Red-Team Probes

```console
(venv) $ python red_team/run_pyrit.py
(venv) $ HARDENED=1 python red_team/run_pyrit.py
```

`HARDENED=1` switches on a stricter system prompt and a recipient allowlist.
Model replies vary between runs, so run each command a few times before you
trust a result.
