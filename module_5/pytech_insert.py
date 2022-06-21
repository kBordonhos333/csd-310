# KBordonhos Module 5.3 assignment
# June 18, 2022

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
Baggins = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins"
    }
Froggins = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Froggins"
    }

print("\n  -- INSERT STATEMENTS --")
Oakenshield_student_id = students.insert_one(Oakenshield).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(Oakenshield_student_id))

Baggins_student_id = students.insert_one(Baggins).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(Baggins_student_id))

Froggins_student_id = students.insert_one(Froggins).inserted_id
print("  Inserted student record Frodo Froggins into the students collection with document_id " + str(Froggins_student_id))

input("\n\n  End of program, press any key to exit... ")