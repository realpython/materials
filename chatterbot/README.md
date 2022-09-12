# Build a Chatbot with Python and Chatterbot

This repository contains code related to the tutorial on [building a Python chatbot with chatterbot](#todo).

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), then install the necessary dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install chatterbot pytz
```

Then you can train and start the interactive CLI bot by running `bot.py`:

```sh
(venv) $ python bot.py
```

After training, you'll see an interactive prompt that you can chat with:

```text
> sure
🤖 when do we want to leave on friday?
> midday sounds good
🤖 Nice that works quite well
> ok for me too
🤖 Yes, but if you don't come with me it's not so smart 😅
> yeah I'll come no worries
🤖 Standing on the Isar cycle path
> where's that?
🤖 ah damn, yes
> a dam? yes?
🤖 a bit madig
```

The bot will learn from the replies you give and improve its accuracy. You can quite the interactive prompt by typing any of the `exit_conditions` defined in `bot.py`.
