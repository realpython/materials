# Minimax in Python: Learn How to Lose the Game of Nim

Here you can find supplementary material for the Real Python tutorial [Minimax in Python: Learn How to Lose the Game of Nim](https://realpython.com/python-minimax-nim/).

This directory contains source code from the tutorial. Additionally, [`nim/`](nim/) contains an implementation of a small game engine that allows you to play Nim against a minimax player.

Run the game as follows:

```console
$ cd nim/
$ python nim.py
```

Make your choices by entering a corresponding character and hit enter. You can choose between the different variants that are described in the tutorial.

If you want to add a variant yourself, you can do so by adding a new file named with a `game_` prefix. Inside this file you need to implement the following functions:

- `initial_state()` should set up the initial game state
- `possible_new_states(state)` should list the possible states you can move to from the current state
- `evaluate(state, is_maximizing)` should evaluate an end game state and return `None` if the game is not over

See the existing `game_*.py` files for examples.

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
