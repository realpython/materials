# RP To-Do

**RP To-Do** is a command-line interface application built with [Typer](https://typer.tiangolo.com/) to help you manage your to-do list.

## Installation

To run **RP To-Do**, you need to run the following steps:

1. Download the application's source code to a `rptodo_project/` directory
2. Create a Python virtual environment and activate it

```sh
$ cd rptodo_project/
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the dependencies

```sh
(venv) $ python -m pip install -r requirements.txt
```

3. Initialize the application

```sh
(venv) $ python -m rptodo init
```

This command asks you to introduce the file path to store the application's database. You can also accept the default file path by pressing enter.

## Usage

Once you've download the source code and run the installation steps, you can run the following command to access the application's usage description:

```sh
$ python -m rptodo --help
Usage: rptodo [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.

Commands:
  add       Add a new to-do with a DESCRIPTION.
  clear     Remove all to-dos.
  complete  Complete a to-do by setting it as done using its TODO_ID.
  init      Initialize the to-do database.
  list      List all to-dos.
  remove    Remove a to-do using its TODO_ID.
```

You can also access the help message for specific commands by typing the command and then `--help`. For example, to display the help content for the `add` command, you can run the following:

```sh
$ python -m rptodo add --help
Usage: rptodo add [OPTIONS] DESCRIPTION...

  Add a new to-do with a DESCRIPTION.

Arguments:
  DESCRIPTION...  [required]

Options:
  -p, --priority INTEGER RANGE  [default: 2]
  --help                        Show this message and exit.
```

Calling `--help` on each command provides specific and useful information about how to use the command at hand.

## Features

**RP To-Do** has the following features:

| Command            | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| `init`             | Initializes the application's to-do database.                |
| `add DESCRIPTION`  | Adds a new to-do to the database with a `DESCRIPTION`.       |
| `list`             | Lists all the to-dos in the database.                        |
| `complete TODO_ID` | Completes a to-do by setting it as done using its `TODO_ID`. |
| `remove TODO_ID`   | Removes a to-do from the database using its `TODO_ID`.       |
| `clear`            | Removes all the to-dos by clearing the database.             |

## Release History

- 0.1.0
  - A work in progress

## About the Author

Leodanis Pozo Ramos - Email: leodanis@realpython.com
