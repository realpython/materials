# ChatterBot: Build a Chatbot with Python

This repository contains code related to the tutorial on [building a Python chatbot with ChatterBot](https://realpython.com/build-a-chatbot-python-chatterbot/).

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), then install the necessary dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
(venv) $ python -m spacy download en_core_web_sm
```

Starting in `source_code_step_5/`, training is handled by a dedicated script, `trainer.py`, that reads from `chat.txt` and populates `db.sqlite3`. The interactive chatbot lives in `bot.py`:

```sh
(venv) $ cd source_code_final
(venv) $ python trainer.py     # (optional) retrain from chat.txt
(venv) $ python bot.py
```

A pretrained `db.sqlite3` is included in each step folder, so you can run `bot.py` right away without retraining.

After training, you'll see an interactive prompt that you can chat with:

```text
> hi
🪴 Hi! How's your day going so far?
> Do you talk to your plants?
🪴 I do!
> What do they like to hear?
🪴 Motivational speeches
> Do plants need sunlight?
🪴 Yes, most plants need sunlight to undergo photosynthesis,
which is how they make their own food. How's your indoor garden doing?
```

The bot will learn from the replies you give and improve its accuracy. You can quit the interactive prompt by typing any of the `exit_conditions` defined in `bot.py`.

## Folder Structure

You'll find the code for each step of the tutorial in a separate folder. The folders also include a SQLite database that contains the different phases of training at each step. Because of this, you can inspect the project at different stages and notice how it evolves when you add more data and interactions.

- `source_code_step_1/` — minimal chatbot with no training
- `source_code_step_2/` — adds `ListTrainer` with a couple of sample exchanges
- `source_code_step_3/` — includes the WhatsApp `chat.txt` export
- `source_code_step_4/` — adds `cleaner.py` for preprocessing the chat export
- `source_code_step_5/` — splits training into `trainer.py` which trains on the cleaned chat data
- `source_code_step_6/` — adds a local LLM via `OllamaLogicAdapter` (requires Ollama)
- `source_code_final/` — same as step 6

## Using the Ollama integration (step 6 and final)

Step 6 and the `source_code_final/` folder use ChatterBot's experimental [Ollama](https://ollama.com/) integration. To try it, [install Ollama](https://realpython.com/ollama/) on your system and pull a small model:

```sh
$ ollama pull llama3.2:latest
```

Then run `bot.py` as usual. If you don't want to use Ollama, remove the `OllamaLogicAdapter` entry from the `logic_adapters` list in `bot.py`.
