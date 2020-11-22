import pymongo

client = pymongo.MongoClient("mongodb+srv://redants:disruptiveCaribbean@whtatsappdev.e5gab.azure.mongodb.net/ANPD?retryWrites=true&w=majority")
db = client["ANPD"]
collection = db["Plates"]

def insertToDB(document):
    InsertedResult = collection.insert_one(document.dict())
    return InsertedResult.inserted_id