# Python Web Applications: Deploy Your Script as a Flask App

Code snippets supplementing the [Python Web Applications: Deploy Your Script as a Flask App](https://realpython.com/python-web-applications/) tutorial.

## Running Locally

Create and activate a Python virtual environment:

```shell
$ python -m venv venv
$ source venv/bin/activate
```

Update `pip` and install the required dependencies:

```shell
(venv) $ pip install -U pip
(venv) $ pip install -r requirements.txt
```

Start the Flask server:

```shell
(venv) $ python main.py
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8080
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 936-229-353
```

Navigate your web browser to this address: <http://127.0.0.1:8080/>
