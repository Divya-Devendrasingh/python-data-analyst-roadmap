# ==========================================
# Module 1: Python Basics
# Topic: if...else Statement
# ==========================================

"""
Definition:
The if...else statement is used to execute one block of
code when a condition is True and another block when the
condition is False.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand the if...else statement.
# 2. Execute different code blocks based on conditions.
# 3. Write simple decision-making programs.

# ==========================================
# Syntax
# ==========================================

# if condition:
#     statement
# else:
#     statement

# ==========================================
# Example 1: Voting Eligibility
# ==========================================

age = 20

print("Example 1")

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# ==========================================
# Example 2: Even or Odd
# ==========================================

number = 15

print("\nExample 2")

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# ==========================================
# Example 3: Pass or Fail
# ==========================================

marks = 35

print("\nExample 3")

if marks >= 40:
    print("Pass")
else:
    print("Fail")

# ==========================================
# Example 4: Positive or Negative
# ==========================================

value = -10

print("\nExample 4")

if value >= 0:
    print("Positive Number")
else:
    print("Negative Number")

# ==========================================
# Example 5: Login Verification
# ==========================================

username = "admin"

print("\nExample 5")

if username == "admin":
    print("Login Successful")
else:
    print("Invalid Username")

# ==========================================
# Example 6: Membership Check
# ==========================================

skills = ["Python", "SQL", "Power BI"]

print("\nExample 6")

if "Python" in skills:
    print("Python Skill Found")
else:
    print("Python Skill Not Found")

# ==========================================
# Practical Example
# ==========================================

balance = 2500

print("\nPractical Example")

if balance >= 1000:
    print("Transaction Approved")
else:
    print("Insufficient Balance")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# if age >= 18
#     print("Eligible")
# else
#     print("Not Eligible")

# Correct:
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

print("\nReturn Type")
print(type(age >= 18))

# ==========================================
# Best Practices
# ==========================================

# ✔ Write clear conditions.
# ✔ Maintain proper indentation.
# ✔ Use meaningful variable names.

# ==========================================
# Practice Questions
# ==========================================

# 1. Check if a number is even or odd.
# 2. Check whether a student passed or failed.
# 3. Check voting eligibility.
# 4. Check whether a number is positive or negative.
# 5. Check whether a skill exists in a list.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is the difference between if and if...else?
# Q2. Can an else statement exist without if?
# Q3. Why is indentation important?
# Q4. What happens if the condition is False?
# Q5. Where is if...else used in real-world applications?

# ==========================================
# End of File
# ==========================================