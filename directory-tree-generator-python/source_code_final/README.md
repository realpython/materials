# RP Tree

RP Tree is a command-line tool to generate a directory tree diagram.

## Run the App

To run **RP Tree**, you need to download the source code. Then open a terminal or command-line window and run the following steps:

1. Create and activate a Python virtual environment.

```sh
$ cd rptree_project/
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Run the application.

```sh
(venv) $ python tree.py /path/to/directory/
```

**Note:** The `-h` or `--help` option provides help on how to use RP Tree.

To take a quick test on **RP Tree**, you can use the sample `home/` directory provided along with the application's code and run the following command:

```sh
(venv) $ python tree.py ../hello/
../hello/
│
├── hello/
│   ├── __init__.py
│   └── hello.py
│
├── tests/
│   └── test_hello.py
│
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

That's it! You've generated a nice directory tree diagram.

## Current Features

If you run RP Tree with a directory path as an argument, then you get the full directory tree printed on your screen. The default input directory is your current directory.

RP Tree also provides the following options:

- `-v`, `--version` shows the application version and exits
- `-h`, `--help` shows a usage message
- `-d`, `--dir-only` generates a directory-only tree
- `-o`, `--output-file` generates a tree and save it to a file in markdown format

## Release History

- 0.1.0
  - A work in progress

## About the Author

Leodanis Pozo Ramos - Email: leodanis@realpython.com
