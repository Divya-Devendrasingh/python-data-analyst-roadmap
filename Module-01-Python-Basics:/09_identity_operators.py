# ==========================================
# Module 1: Python Basics
# Topic: Identity Operators
# ==========================================

"""
Definition:
Identity operators are used to check whether two variables
refer to the same object in memory.

Python provides two identity operators:
1. is
2. is not
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand identity operators.
# 2. Learn the difference between == and is.
# 3. Compare objects using is and is not.

# ==========================================
# Variables
# ==========================================

a = [10, 20, 30]
b = a
c = [10, 20, 30]

# ==========================================
# is Operator
# ==========================================

print("is Operator")

print(f"a is b : {a is b}")
print(f"a is c : {a is c}")

# ==========================================
# is not Operator
# ==========================================

print("\nis not Operator")

print(f"a is not b : {a is not b}")
print(f"a is not c : {a is not c}")

# ==========================================
# Difference Between == and is
# ==========================================

print("\nDifference Between == and is")

print(f"a == b : {a == b}")
print(f"a == c : {a == c}")

print(f"a is b : {a is b}")
print(f"a is c : {a is c}")

# ==========================================
# Identity with Numbers
# ==========================================

x = 100
y = 100

print("\nIdentity with Numbers")

print(f"x is y : {x is y}")
print(f"x == y : {x == y}")

# ==========================================
# Identity with Strings
# ==========================================

name1 = "Python"
name2 = "Python"

print("\nIdentity with Strings")

print(f"name1 is name2 : {name1 is name2}")
print(f"name1 == name2 : {name1 == name2}")

# ==========================================
# Practical Example
# ==========================================

employee_list = ["Alice", "Bob"]
backup_list = employee_list
new_list = ["Alice", "Bob"]

print("\nPractical Example")

print(employee_list is backup_list)
print(employee_list is new_list)

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# if a is 10:

# Correct:
# if a == 10:

print("\nReturn Type")
print(type(a is b))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use == to compare values.
# ✔ Use is to compare object identity.
# ✔ Use is when checking for None.

# ==========================================
# Practice Questions
# ==========================================

# 1. Compare two variables using is.
# 2. Compare two variables using is not.
# 3. Compare values using ==.
# 4. Compare lists using == and is.
# 5. Observe the difference in outputs.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What are identity operators?
# Q2. What is the difference between == and is?
# Q3. What does is not do?
# Q4. When should you use is?
# Q5. Why is 'is' commonly used with None?

# ==========================================
# End of File
# ==========================================