# ==========================================
# Module 1: Python Basics
# Topic: if Statement
# ==========================================

"""
Definition:
The if statement is used to execute a block of code only
when a specified condition is True.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand the if statement.
# 2. Write conditional programs.
# 3. Use comparison operators with if.

# ==========================================
# Syntax
# ==========================================

# if condition:
#     statement

# ==========================================
# Example 1: Basic if Statement
# ==========================================

age = 20

print("Example 1")

if age >= 18:
    print("Eligible to vote")

# ==========================================
# Example 2: Number Check
# ==========================================

number = 15

print("\nExample 2")

if number > 0:
    print("Positive Number")

# ==========================================
# Example 3: Marks Check
# ==========================================

marks = 85

print("\nExample 3")

if marks >= 40:
    print("Pass")

# ==========================================
# Example 4: Salary Check
# ==========================================

salary = 60000

print("\nExample 4")

if salary > 50000:
    print("High Salary")

# ==========================================
# Example 5: String Comparison
# ==========================================

language = "Python"

print("\nExample 5")

if language == "Python":
    print("Learning Python")

# ==========================================
# Example 6: Multiple Conditions
# ==========================================

age = 25
salary = 70000

print("\nExample 6")

if age >= 18 and salary >= 50000:
    print("Eligible")

# ==========================================
# Example 7: Membership Operator
# ==========================================

skills = ["Python", "SQL", "Power BI"]

print("\nExample 7")

if "Python" in skills:
    print("Python Skill Found")

# ==========================================
# Practical Example
# ==========================================

balance = 5000

print("\nPractical Example")

if balance >= 1000:
    print("Sufficient Balance")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# if age >= 18
#     print("Eligible")

# Correct:
# if age >= 18:
#     print("Eligible")

print("\nBoolean Check")
print(type(age >= 18))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use meaningful conditions.
# ✔ Indent code correctly.
# ✔ Keep conditions simple and readable.

# ==========================================
# Practice Questions
# ==========================================

# 1. Check if a person is eligible to vote.
# 2. Check if a number is positive.
# 3. Check if marks are greater than or equal to 35.
# 4. Check if a skill exists in a list.
# 5. Check if salary is greater than ₹50,000.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is an if statement?
# Q2. Why is indentation important in Python?
# Q3. Can an if statement exist without else?
# Q4. What data type should an if condition return?
# Q5. Where are if statements commonly used?

# ==========================================
# End of File
# ==========================================