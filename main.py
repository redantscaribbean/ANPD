import os
from flask import Flask, request, render_template
import requests
import pymongo
import Models.LicensePlate as LicensePlate
import json

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://redants:disruptiveCaribbean@whtatsappdev.e5gab.azure.mongodb.net/ANPD?retryWrites=true&w=majority")
db = client["ANPD"]
collection = db["Plates"]
LicensePlate = LicensePlate.LicensePlate()


@app.route('/webhook', methods=['POST'])
def handle_form():
    header = request.headers["Content-Type"]
    dataReceived = request.values.get("json")
    PlateInfo = json.loads(dataReceived)
    plate = PlateInfo["data"]["results"][0]["plate"]
    LicensePlate.plate = plate
    print (plate)
    collection.insert_one(LicensePlate.dict())
    return "Ok"


@app.route("/")
def index():
    return render_template("index.html");   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)