import os
from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def handle_form():
    header = request.headers["Content-Type"]
    key_1 = request.values.get("json")
    print (key_1)
    return "Ok"


@app.route("/")
def index():
    return render_template("index.html");   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)