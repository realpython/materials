# Flask Series: Sample Project

This repository contains the code for the `board` Flask sample project.

## Setup

You can run the provided example project on your local machine by following the steps outlined below.

Create a new virtual environment:

```bash
python3 -m venv venv/
```

Activate the virtual environment:

```bash
source ./venv/bin/activate
```

Navigate to the folder for the step that you're currently on.

Install the dependencies for this project if you haven't installed them yet:

```bash
(venv) $ python -m pip install -r requirements.txt
```

### Environment Variables

This project works with environment variables that the application expects in a `.env` file inside the root directory of your project.

Create a `.env` file with this content:

```
FLASK_SECRET_KEY="mysecretkey"
FLASK_DATABASE="board.sqlite"
```

You can add your own content there, but you must define it before running the Flask application.

#### Secret Key

If you want to deploy your Flask app later, then it's a good idea to generate a proper secret key.

If you need to create cryptographically sound data like a Flask secret key, then you can use Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module:

```pycon
>>> import secrets
>>> secrets.token_hex()
'2e9ac41b1e0b66a8d93d66400e2300c4b4c2953f'
```

The `.token_hex()` method returns a [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) string containing random numbers and letters from `0` to `9` and `a` to `f`. Use the value that `secrets.token_hex()` outputs for you and add it to your Flask project's `.env` file:

```
# .env

FLASK_SECRET_KEY="2e9ac41b1e0b66a8d93d66400e2300c4b4c2953f"
FLASK_DATABASE="board.sqlite"

```

To avoid saving the secret key directly in your code, it may be a good idea to work with [environment variables](https://12factor.net/config). You can learn more about that in the Flask documentation on [configuration handling](https://flask.palletsprojects.com/en/2.3.x/config/).

## Development Server

To run the Flask development server, enter this command in your terminal while being in the root directory of your project:

```bash
(venv) $ python -m flask --app board run --debug
```

Now you can navigate to the address that's shown in the output when you start the server. Commonly, that's `http://localhost:5000/`.
