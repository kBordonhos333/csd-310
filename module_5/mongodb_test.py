# creating mongodb client

from pymongo import MongoClient
import pymongo
	
# mongodb atlas url to connect python to mongodb using pymongo
url = "mongodb+srv://admin:admin@cluster0.ml5p53p.mongodb.net/?retryWrites=true&w=majority"

# create connection using MongoClient
from pymongo import MongoClient
client = MongoClient(url)

# variable named db assigned to pytech database instance
db = client.pytech

print(db.list_collection_names())



