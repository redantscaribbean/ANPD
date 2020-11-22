import requests
from azure.servicebus import QueueClient, Message
import json
import PublishResults

# Create the QueueClient
queue_client = QueueClient.from_connection_string("Endpoint=sb://licenseplate.servicebus.windows.net/;SharedAccessKeyName=Listen;SharedAccessKey=ppfUqRsh3R7CFGmYXxing8/DT9BB+uSnqL6YnAMZbHE=;EntityPath=licenseplates", "licenseplates")


def ReceivePlateInfo():
    while (True):
        with queue_client.get_receiver() as queue_receiver:
            messages = queue_receiver.fetch_next(timeout=3)
            for message in messages:
                res = requests.post('http://anpd.eastus.cloudapp.azure.com:8000/PublishResults', json=str(message))
                message.complete()


ReceivePlateInfo()
