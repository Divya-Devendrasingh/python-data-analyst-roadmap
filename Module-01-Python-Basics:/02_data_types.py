# ==========================================
# Module 1: Python Basics
# Topic: Data Types
# ==========================================

"""
Definition:
A data type specifies the type of value stored in a variable.

Python automatically identifies the data type based on the value assigned.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand Python's basic data types.
# 2. Learn how to check a variable's data type.
# 3. Learn type conversion.

# ==========================================
# Integer (int)
# ==========================================

age = 25

print("Integer Value:", age)
print("Data Type:", type(age))

# ==========================================
# Float
# ==========================================

price = 499.99

print("\nFloat Value:", price)
print("Data Type:", type(price))

# ==========================================
# String (str)
# ==========================================

course = "Python"

print("\nString Value:", course)
print("Data Type:", type(course))

# ==========================================
# Boolean (bool)
# ==========================================

is_completed = True

print("\nBoolean Value:", is_completed)
print("Data Type:", type(is_completed))

# ==========================================
# Checking Data Types
# ==========================================

number = 100
decimal = 10.5
text = "Data Analyst"

print("\nChecking Data Types")
print(type(number))
print(type(decimal))
print(type(text))

# ==========================================
# Type Conversion
# ==========================================

# String to Integer

num = "100"
converted_num = int(num)

print("\nString to Integer")
print(converted_num)
print(type(converted_num))

# Integer to Float

marks = 95
converted_marks = float(marks)

print("\nInteger to Float")
print(converted_marks)
print(type(converted_marks))

# Float to Integer

salary = 55000.75
converted_salary = int(salary)

print("\nFloat to Integer")
print(converted_salary)
print(type(converted_salary))

# Integer to String

year = 2026
converted_year = str(year)

print("\nInteger to String")
print(converted_year)
print(type(converted_year))

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# age = "25"
# print(age + 5)

# Correct:
age = int("25")
print("\nCorrect Addition:", age + 5)

# ==========================================
# Best Practices
# ==========================================

# Use meaningful variable names.
# Choose the correct data type for the data.
# Convert data types only when required.

# ==========================================
# Practice Questions
# ==========================================

# 1. Create one variable of each data type.
# 2. Convert "250" into an integer.
# 3. Convert 75 into a string.
# 4. Convert 45 into a float.
# 5. Print the data type of each variable.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What are Python's basic data types?
# Q2. What is the difference between int and float?
# Q3. What does type() do?
# Q4. What is type conversion?
# Q5. How do you convert a string into an integer?

# ==========================================
# End of File
# ==========================================