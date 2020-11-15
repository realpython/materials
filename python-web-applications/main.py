from flask import Flask
from flask import request

app = Flask(__name__)


def convert_temp(cel_temp):
    """Converts Celsius temperature to Fahrenheit temperature."""
    try:
        far_temp = float(cel_temp) * 9 / 5 + 32
        far_temp = round(far_temp, 3)  # Round to three decimal places
        return str(far_temp)
    except ValueError:  # User entered non-numeric temperature
        return "invalid input"


@app.route("/")
def index():
    cel_temp = request.args.get("cel_temp")
    if cel_temp:
        far_temp = convert_temp(cel_temp)
    else:
        far_temp = ""
    return (
        """<form action="">
                Celsius: <input type="text" name="cel_temp">
                <input type="submit" value="Convert">
            </form>"""
        + "Fahrenheit: "
        + far_temp
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
