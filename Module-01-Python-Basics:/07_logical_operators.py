# ==========================================
# Module 1: Python Basics
# Topic: Logical Operators
# ==========================================

"""
Definition:
Logical operators are used to combine two or more conditions.
They always return a Boolean value (True or False).
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand logical operators.
# 2. Learn AND, OR and NOT.
# 3. Combine multiple conditions.

# ==========================================
# Variables
# ==========================================

age = 25
salary = 60000

# ==========================================
# Logical AND
# ==========================================

print("Logical AND")

print(age > 18 and salary > 50000)
print(age > 18 and salary > 70000)

# ==========================================
# Logical OR
# ==========================================

print("\nLogical OR")

print(age > 18 or salary > 70000)
print(age < 18 or salary > 70000)

# ==========================================
# Logical NOT
# ==========================================

print("\nLogical NOT")

print(not(age > 18))
print(not(age < 18))

# ==========================================
# Combining Multiple Conditions
# ==========================================

marks = 85
attendance = 90

print("\nMultiple Conditions")

print(marks >= 40 and attendance >= 75)
print(marks >= 90 or attendance >= 90)

# ==========================================
# Practical Example
# ==========================================

username = "admin"
password = "python123"

print("\nLogin Verification")

print(username == "admin" and password == "python123")
print(username == "admin" and password == "password")

# ==========================================
# Boolean Expressions
# ==========================================

is_logged_in = True
is_verified = False

print("\nBoolean Expressions")

print(is_logged_in and is_verified)
print(is_logged_in or is_verified)
print(not is_verified)

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# age > 18 & salary > 50000

# Correct:
# age > 18 and salary > 50000

print("\nReturn Type")
print(type(age > 18 and salary > 50000))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use parentheses for complex conditions.
# ✔ Use 'and', 'or', and 'not' instead of &, |, and !.
# ✔ Keep conditions readable.

# ==========================================
# Practice Questions
# ==========================================

# 1. Check whether a number is positive and even.
# 2. Check whether a student passed using marks and attendance.
# 3. Use OR to check two conditions.
# 4. Use NOT to reverse a Boolean value.
# 5. Combine three conditions using AND.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What are logical operators?
# Q2. Explain AND, OR and NOT.
# Q3. What data type do logical operators return?
# Q4. What is the difference between AND and OR?
# Q5. Where are logical operators used?

# ==========================================
# End of File
# ==========================================