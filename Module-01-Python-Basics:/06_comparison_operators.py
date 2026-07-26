# ==========================================
# Module 1: Python Basics
# Topic: Comparison Operators
# ==========================================

"""
Definition:
Comparison operators are used to compare two values.
They always return a Boolean value: True or False.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand comparison operators.
# 2. Learn Boolean results.
# 3. Use comparison operators in conditions.

# ==========================================
# Equal To (==)
# ==========================================

a = 20
b = 10

print("Equal To (==)")
print(f"{a} == {b} : {a == b}")

# ==========================================
# Not Equal To (!=)
# ==========================================

print("\nNot Equal To (!=)")
print(f"{a} != {b} : {a != b}")

# ==========================================
# Greater Than (>)
# ==========================================

print("\nGreater Than (>)")
print(f"{a} > {b} : {a > b}")

# ==========================================
# Less Than (<)
# ==========================================

print("\nLess Than (<)")
print(f"{a} < {b} : {a < b}")

# ==========================================
# Greater Than or Equal To (>=)
# ==========================================

print("\nGreater Than or Equal To (>=)")
print(f"{a} >= {b} : {a >= b}")

# ==========================================
# Less Than or Equal To (<=)
# ==========================================

print("\nLess Than or Equal To (<=)")
print(f"{a} <= {b} : {a <= b}")

# ==========================================
# Comparison with Strings
# ==========================================

name1 = "Alice"
name2 = "Bob"

print("\nComparison with Strings")
print(f"{name1} == {name2} : {name1 == name2}")
print(f"{name1} != {name2} : {name1 != name2}")

# ==========================================
# Comparison with Numbers
# ==========================================

marks = 85

print("\nComparison with Numbers")
print(f"marks >= 40 : {marks >= 40}")
print(f"marks < 40 : {marks < 40}")

# ==========================================
# Practical Example
# ==========================================

salary = 60000

print("\nPractical Example")
print(f"Salary > 50000 : {salary > 50000}")
print(f"Salary == 60000 : {salary == 60000}")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# if a = b:

# Correct:
# if a == b:

print("\nComparison Returns Boolean")
print(type(a > b))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use == for comparison.
# ✔ Use = only for assignment.
# ✔ Write meaningful comparison expressions.

# ==========================================
# Practice Questions
# ==========================================

# 1. Compare two numbers using ==.
# 2. Compare two numbers using !=.
# 3. Check if one number is greater than another.
# 4. Compare two strings.
# 5. Check if a number is greater than or equal to 100.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What are comparison operators?
# Q2. What is the difference between = and ==?
# Q3. Which data type do comparison operators return?
# Q4. Explain >= and <=.
# Q5. Where are comparison operators commonly used?

# ==========================================
# End of File
# ==========================================