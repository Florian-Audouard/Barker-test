import os
from flask import Flask, jsonify, render_template, request

os.chdir(os.path.dirname(__file__))


app = Flask(__name__)


@app.route("/")
def index():  # pylint: disable=missing-function-docstring
    return render_template("index.html")


@app.route("/msgFromServer", methods=["POST"])
def send_msg():  # pylint: disable=missing-function-docstring
    data = request.get_data()
    number = int(data)
    msg = []
    with open("./save.txt", "r", encoding="utf-8") as file:
        for x in file:
            msg.append(x.replace("\n", ""))
    print(msg)
    if number == len(msg):
        return jsonify("no")
    print(msg[number : len(msg)])
    return jsonify(msg[number : len(msg)])


@app.route("/msgFromHtml", methods=["POST"])
def receive_msg():  # pylint: disable=missing-function-docstring
    result = request.get_data()
    with open("./save.txt", "a", encoding="utf-8") as file:
        file.write(result.decode("utf-8") + "\n")
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
