# RP Dice Roller

RP Dice Roller is a small Python app that simulates dice rolling events. This code supplements the article [Build a Dice-Rolling Application With Python](https://realpython.com/python-dice-roll/) on realpython.com.

## Running RP Dice Roller

The project's code was tested with Python 3.9.5. However, it should work with any Python versions greater than or equal to 3.6. There are no external dependencies. To run the project's code, execute the following command with the appropriate Python interpreter:

```sh
$ python dice.py
How many dice do you want to roll? [1-6] 5

~~~~~~~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~~~~~~~
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│  ●   ●  │ │  ●      │ │  ●   ●  │ │  ●   ●  │ │         │
│    ●    │ │         │ │    ●    │ │    ●    │ │    ●    │
│  ●   ●  │ │      ●  │ │  ●   ●  │ │  ●   ●  │ │         │
└─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
```

The application prompts the user for the number of dice they want to roll and generates a dice faces ASCII diagram with the results.

Each folder in this repository contains the code for the corresponding step in the companion article in a file called `dice.py`.
