"""
Module 2 - Dictionaries

Topics Covered:
- Creating Dictionaries
- Accessing Values
- Adding & Updating
- keys()
- values()
- items()
- get()
- update()
- pop()
- clear()
"""

student = {
    "id": 101,
    "name": "Rahul",
    "course": "Python"
}

print(student)

print(student["name"])

student["course"] = "Data Analytics"

student["city"] = "Hyderabad"

print(student)

print(student.keys())

print(student.values())

print(student.items())

print(student.get("name"))

student.update({"age": 22})

print(student)

student.pop("city")

print(student)

print(len(student))

print("name" in student)

student.clear()

print(student)