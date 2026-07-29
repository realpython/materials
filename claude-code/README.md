# How to Use Claude Code to Write and Refactor Python

This folder contains code associated with the Real Python tutorial [How to Use Claude Code to Write and Refactor Python](https://realpython.com/how-to-use-claude-code/).

The `mini-contacts/` project is the finished state of the command-line contact manager that you build with Claude Code in the tutorial. The prompts that produced it are collected in [`prompts.md`](prompts.md), in the order they appear.

Because Claude Code is nondeterministic, your own run won't match this code line for line. Expect the same structure, a storage module for CSV operations and a CLI module for argument parsing, with different naming and implementation details.

## Run the Project

```sh
$ cd mini-contacts/
$ python -m mini_contacts add --name "Alice" --email "alice@example.com" --phone "555-1234"
$ python -m mini_contacts list
```

Contacts are stored at `~/.mini-contacts.csv` by default. Pass `--path` to use a different file.

## Run the Tests

```sh
$ cd mini-contacts/
$ python -m unittest
```

The suite uses `unittest` from the standard library, so there's nothing to install.

## About the Author

Real Python - Email: office@realpython.com

## License

Distributed under the MIT license. See `LICENSE` for more information.
