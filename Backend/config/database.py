from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@sistemapresenca.6nhyo7m.mongodb.net/?retryWrites=true&w=majority&appName=SistemaPresenca")

db = client.presence_db
db2 = client.user_db

collection_presence = db["presence_collection"]
collection_user = db2["user_collection"]