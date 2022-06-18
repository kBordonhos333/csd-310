

from pymongo import MongoClient
 
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")

db = conn.pytech

students = db.students

student = students.find()
for id in student:
    print(id)