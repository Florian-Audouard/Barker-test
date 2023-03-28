import os
from flask import Flask, jsonify, render_template

os.chdir(os.path.dirname(__file__))


app = Flask(__name__)


@app.route("/")
def index():  # pylint: disable=missing-function-docstring
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
