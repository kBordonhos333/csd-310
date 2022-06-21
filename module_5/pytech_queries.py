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

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

Oakenshield = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + Oakenshield["student_id"] + "\n  First Name: " + Oakenshield["first_name"] + "\n  Last Name: " + Oakenshield["last_name"] + "\n")