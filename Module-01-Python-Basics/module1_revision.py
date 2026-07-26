"""
=========================================
Module 1 : Python Basics Revision
Python for Data Analyst Roadmap
=========================================
Topics Covered
--------------
1. Variables
2. Data Types
3. Input / Output
4. Type Casting
5. Operators
6. Conditional Statements
7. Common Errors
8. Strings
9. String Methods
"""

# ----------------------------
# Variables
# ----------------------------

name = "Divya"
age = 27
salary = 35000.50
is_student = False

print(name)
print(age)

# ----------------------------
# Data Types
# ----------------------------

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))

# ----------------------------
# Input & Type Casting
# ----------------------------

marks = int(input("Enter Marks: "))
print("Marks:", marks)

# ----------------------------
# Operators
# ----------------------------

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# ----------------------------
# Comparison Operators
# ----------------------------

print(a > b)
print(a == b)

# ----------------------------
# Conditional Statements
# ----------------------------

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# ----------------------------
# String Indexing
# ----------------------------

text = "Python"

print(text[0])
print(text[-1])

# ----------------------------
# String Slicing
# ----------------------------

print(text[0:3])
print(text[2:])
print(text[::-1])

# ----------------------------
# String Methods
# ----------------------------

email = "  DIVYA@GMAIL.COM  "

email = email.strip()
email = email.lower()

print(email)

name = "python"

print(name.upper())
print(name.lower())

sentence = "I love Python"

print(sentence.replace("Python", "SQL"))

skills = "Python,SQL,Power BI"

print(skills.split(","))

print(sentence.find("love"))
print(sentence.count("o"))

filename = "report.csv"

print(filename.startswith("report"))
print(filename.endswith(".csv"))

print(len(sentence))

print("Module 1 Completed Successfully!")