from flask import Flask

app = Flask(__name__)

if app.debug:

    def count_visitor():
        ...

else:
    import count_visitor


@app.route("/")
def home():
    count_visitor()
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
