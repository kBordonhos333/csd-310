#KBordonhos Module 5.3 assignment

from pymongo import MongoClient
 
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")
   
db = conn.pytech

students = db.students

Oakenshield = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield"
    }

Oakenshield_student_id = students.insert_one(Oakenshield).inserted_id

Baggins = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins"
    }

Baggins_student_id = students.insert_one(Baggins).inserted_id

Froggins = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Froggins"
    }

Froggins_student_id = students.insert_one(Froggins).inserted_id

print(f"\nInserted student record", Oakenshield, Oakenshield_student_id)
print(f"\nInserted student record", Baggins, Baggins_student_id)
print(f"\nInserted student record", Froggins, Froggins_student_id)
