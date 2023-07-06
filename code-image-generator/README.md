# Build a Code Image Generator with Flask, Pygments, and Playwright

Follow the [step-by-step instructions](https://realpython.com/code-image-generator/) on Real Python.

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

Navigate to the folder for the step you're currently on.

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
(venv) $ flask run
```

Now you can navigate to the address that's shown in the output when you start the server. Commonly, that's `http://localhost:5000/`.
