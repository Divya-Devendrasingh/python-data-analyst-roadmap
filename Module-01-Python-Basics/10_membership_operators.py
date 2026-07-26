# ==========================================
# Module 1: Python Basics
# Topic: Membership Operators
# ==========================================

"""
Definition:
Membership operators are used to check whether a value
exists in a sequence such as a string, list, tuple,
set, or dictionary.

Python provides two membership operators:
1. in
2. not in
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand membership operators.
# 2. Learn 'in' and 'not in'.
# 3. Check values in different data structures.

# ==========================================
# Membership in List
# ==========================================

languages = ["Python", "SQL", "Power BI", "Excel"]

print("Membership in List")

print(f"'Python' in languages : {'Python' in languages}")
print(f"'Java' in languages : {'Java' in languages}")

# ==========================================
# not in Operator
# ==========================================

print("\nnot in Operator")

print(f"'Java' not in languages : {'Java' not in languages}")
print(f"'SQL' not in languages : {'SQL' not in languages}")

# ==========================================
# Membership in String
# ==========================================

course = "Python Programming"

print("\nMembership in String")

print(f"'Python' in course : {'Python' in course}")
print(f"'Java' in course : {'Java' in course}")

# ==========================================
# Membership in Tuple
# ==========================================

numbers = (10, 20, 30, 40)

print("\nMembership in Tuple")

print(f"20 in numbers : {20 in numbers}")
print(f"100 in numbers : {100 in numbers}")

# ==========================================
# Membership in Set
# ==========================================

skills = {"Python", "SQL", "Excel"}

print("\nMembership in Set")

print(f"'SQL' in skills : {'SQL' in skills}")
print(f"'Tableau' in skills : {'Tableau' in skills}")

# ==========================================
# Membership in Dictionary
# ==========================================

student = {
    "name": "Alice",
    "age": 24,
    "city": "Delhi"
}

print("\nMembership in Dictionary")

print(f"'name' in student : {'name' in student}")
print(f"'marks' in student : {'marks' in student}")

# ==========================================
# Practical Example
# ==========================================

required_skills = ["Python", "SQL", "Power BI"]

candidate_skill = "SQL"

print("\nPractical Example")

print(f"Does the candidate know {candidate_skill}?")
print(candidate_skill in required_skills)

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# if "Python" == languages

# Correct:
# if "Python" in languages

print("\nReturn Type")
print(type("Python" in languages))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use 'in' to check whether an item exists.
# ✔ Use 'not in' to check whether an item is absent.
# ✔ Membership operators return Boolean values.

# ==========================================
# Practice Questions
# ==========================================

# 1. Check if a number exists in a list.
# 2. Check if a character exists in a string.
# 3. Check if a key exists in a dictionary.
# 4. Use 'not in' with a tuple.
# 5. Check whether a skill exists in a set.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What are membership operators?
# Q2. What is the difference between 'in' and 'not in'?
# Q3. Which data structures support membership operators?
# Q4. What data type do membership operators return?
# Q5. How do membership operators work with dictionaries?

# ==========================================
# End of File
# ==========================================