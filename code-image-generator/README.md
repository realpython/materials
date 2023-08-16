# Build a Code Image Generator with Flask, Pygments, and Playwright

Follow the [step-by-step instructions](https://realpython.com/python-code-image-generator/) on Real Python.

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

Next, you need to install Playwright:

```bash
(venv) $  playwright install
```

Finally, run the Flask development server

```bash
(venv) $ python -m flask run
```

Now you can navigate to the address that's shown in the output when you start the server. Commonly, that's `http://localhost:5000/`.

## Secret Key

If you want to deploy your Flask app later, then it's a good idea to generate a proper secret key.

If you need to create cryptographically sound data like a Flask secret key, then you can use Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module:

```pycon
>>> import secrets
>>> secrets.token_hex()
'2e9ac41b1e0b66a8d93d66400e2300c4b4c2953f'
```

The `.token_hex()` method returns a [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) string containing random numbers and letters from `0` to `9` and `a` to `f`. Use the value that `secrets.token_hex()` outputs for you and add it to your Flask project's `app.py` file:

```python hl_lines="6"
# app.py

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "2e9ac41b1e0b66a8d93d66400e2300c4b4c2953f"

# ...
```

To avoid saving the secret key directly in your code, it may be a good idea to work with [environment variables](https://12factor.net/config). You can learn more about that in the Flask documentation on [configuration handling](https://flask.palletsprojects.com/en/2.3.x/config/).
