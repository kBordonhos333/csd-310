# Kelly Bordonhos Module 5.3 assignment
# June 18, 2022

from pymongo import MongoClient
 
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")

print(f"\n")
print("Displaying Students documents from find() query: ")
print(f"\n")
db = conn.pytech

students = db.students

docs = db.students.find({})

for doc in docs:
    print(doc)

doc = db.students.find_one({"student_id": "1007"})
print(f"\n")
print("Displaying student document from find_one() query: ")
print(f"\n")
print(doc)