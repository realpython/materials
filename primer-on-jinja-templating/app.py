from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html", title="Jinja and Flask")


max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine", "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Sirius", "score": 75},
]


@app.route("/results")
def results():
    context = {
        "title": "Results",
        "max_score": max_score,
        "test_name": test_name,
        "students": students,
    }
    return render_template("results.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
