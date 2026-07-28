# ===============================================
# Module 2: Data Structures
# Topic: Mini Project - Student Record Management
# ===============================================


# Student Details (Dictionary)
student = {
    "id": 101,
    "name": "John",
    "age": 21,
    "city": "Delhi"
}

# Marks (List)
marks = [85, 90, 78, 92]

print("Highest Mark:", max(marks))

marks.append(95)
marks.remove(78)

print("Updated Marks:", marks)

# Subjects (Tuple)
subjects = ("Python", "SQL", "Excel", "Power BI")

print("Total Subjects:", len(subjects))
print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

# Skills (Set)
skills = {"Python", "SQL", "Excel"}

skills.add("Power BI")

print("Is Python available?", "Python" in skills)
print("Skills:", skills)

# Dictionary Operations
student.update({"city": "Hyderabad"})
student["course"] = "Data Analyst"

print("\nStudent Keys:")
print(student.keys())

print("\nStudent Values:")
print(student.values())

print("\nStudent Items:")
print(student.items())

print("\nFinal Student Record:")
print(student)