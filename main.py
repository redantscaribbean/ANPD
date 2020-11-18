import os
from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def handle_form():
    data = request.json
    print (data)
    return data


@app.route("/")
def index():
    return render_template("index.html");   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)