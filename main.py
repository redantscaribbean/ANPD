import os
from flask import Flask, request, render_template
import requests
import pymongo
import Models.LicensePlate as LicensePlate
import json
from flask_socketio import SocketIO, send
import AddToQueue
import uuid
import DBHelper

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
app.config['SECRET_KEY'] = 'secret!'

LicensePlate = LicensePlate.LicensePlate()

@app.route('/webhook', methods=['POST'])
def receiveInfo():
    header = request.headers["Content-Type"]
    dataReceived = request.values.get("json") # data is received as Form-Data. json holds the data we want
    PlateInfo = json.loads(dataReceived)
    LicensePlate = buildLicensePlate(PlateInfo) #Build LicensePlate Object with data received
    LicensePlate.inserted_id = str(DBHelper.insertToDB(LicensePlate)) #Insert into DB
    AddToQueue.sendLicensePlateToQueue(LicensePlate) #Send to Queue
    return "Ok"

def buildLicensePlate(PlateInfo):
    LicensePlate.plate = PlateInfo["data"]["results"][0]["plate"]
    LicensePlate.dscore = PlateInfo["data"]["results"][0]["dscore"]
    LicensePlate.score = PlateInfo["data"]["results"][0]["score"]
    LicensePlate.vehicle_type = PlateInfo["data"]["results"][0]["vehicle"]["type"]
    LicensePlate.vehicle_type_score = PlateInfo["data"]["results"][0]["vehicle"]["score"]
    LicensePlate.camera_id = PlateInfo["data"]["camera_id"]
    LicensePlate.filename = PlateInfo["data"]["filename"]
    LicensePlate.timestamp = PlateInfo["data"]["timestamp"]
    return LicensePlate


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=80)