# ==========================================
# Module 1: Python Basics
# Topic: elif Statement
# ==========================================

"""
Definition:
The elif (else if) statement is used to check multiple
conditions. If the first condition is False, Python checks
the next condition, and so on.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand the elif statement.
# 2. Handle multiple conditions.
# 3. Write decision-making programs.

# ==========================================
# Syntax
# ==========================================

# if condition1:
#     statement
# elif condition2:
#     statement
# else:
#     statement

# ==========================================
# Example 1: Grade Classification
# ==========================================

marks = 82

print("Example 1")

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

# ==========================================
# Example 2: Age Category
# ==========================================

age = 24

print("\nExample 2")

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# ==========================================
# Example 3: Temperature Check
# ==========================================

temperature = 30

print("\nExample 3")

if temperature < 15:
    print("Cold")
elif temperature <= 30:
    print("Pleasant")
else:
    print("Hot")

# ==========================================
# Example 4: Salary Category
# ==========================================

salary = 65000

print("\nExample 4")

if salary < 30000:
    print("Low Salary")
elif salary < 60000:
    print("Average Salary")
else:
    print("High Salary")

# ==========================================
# Example 5: Login Role
# ==========================================

role = "Manager"

print("\nExample 5")

if role == "Admin":
    print("Full Access")
elif role == "Manager":
    print("Limited Access")
elif role == "Employee":
    print("Basic Access")
else:
    print("Access Denied")

# ==========================================
# Practical Example
# ==========================================

purchase_amount = 3200

print("\nPractical Example")

if purchase_amount >= 5000:
    discount = 20
elif purchase_amount >= 3000:
    discount = 10
elif purchase_amount >= 1000:
    discount = 5
else:
    discount = 0

print(f"Purchase Amount: ₹{purchase_amount}")
print(f"Discount: {discount}%")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# if marks >= 90:
#     print("A")
# else if marks >= 75:
#     print("B")

# Correct:
# elif marks >= 75:
#     print("B")

print("\nReturn Type")
print(type(marks >= 75))

# ==========================================
# Best Practices
# ==========================================

# ✔ Arrange conditions from most specific to least specific.
# ✔ Avoid unnecessary elif statements.
# ✔ Keep conditions simple and readable.

# ==========================================
# Practice Questions
# ==========================================

# 1. Find the grade based on marks.
# 2. Categorize a person's age.
# 3. Find salary category.
# 4. Determine discount percentage.
# 5. Display user role based on role name.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is the purpose of elif?
# Q2. What is the difference between if, elif, and else?
# Q3. Can multiple elif blocks be used?
# Q4. Is else mandatory in an if...elif statement?
# Q5. When should you use elif instead of multiple if statements?

# ==========================================
# End of File
# ==========================================