from azure.servicebus import QueueClient, Message
import json

# Create the QueueClient
queue_client = QueueClient.from_connection_string("Endpoint=sb://licenseplate.servicebus.windows.net/;SharedAccessKeyName=Sender;SharedAccessKey=TkEAw0ST1O1qufVCNfZstERuyp4iIomRKsTe/x08PrY=", "licenseplates")



def sendLicensePlateToQueue(LicensePlate):
    # Send a test message to the queue
    print(LicensePlate)
    msg = Message(json.dumps(LicensePlate.dict()))
    queue_client.send(msg)