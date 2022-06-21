# KBordonhos Module 6.3 Pytech: Deleting Documents
# June 21, 2022

# Add code to connect to students collection
from pymongo import MongoClient
 
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")
   
db = conn.pytech

students = db.students


# Call find() method and display results before changes
docs = db.students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Call insert() method to insert new document with student_id 1010
Deckard = {
    "student_id": "1010",
    "first_name": "Rick",
    "last_name": "Deckard"
    }

Deckard_student_id = students.insert_one(Deckard).inserted_id

print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(Deckard_student_id))

# Call find_one() method and display results
Deckard = students.find_one({"student_id": "1010"})
print("  Student ID: " + Deckard["student_id"] + "\n  First Name: " + Deckard["first_name"] + "\n  Last Name: " + Deckard["last_name"] + "\n")

# Display results after adding new document with student_id 1010
print("\n -- DISPLAYING NEW STUDENT LIST DOC --")
for doc in docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Call delete_one() method to remove student_id 1010
students.delete_one({"student_id": "1010"})

# Display results after removing document with student_id 1010
print("\n -- DELETED STUDENT ID: 1010 --")
for doc in docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input("\n\n  End of program, press any key to exit... ")