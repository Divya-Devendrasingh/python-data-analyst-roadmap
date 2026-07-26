# ==========================================
# Module 1: Python Basics
# Topic: Variables
# ==========================================

"""
Definition:
A variable is a named container used to store data in memory.
It allows us to save information and use it later in a program.
"""

# ==========================================
# Variable Naming Rules
# ==========================================

# 1. Variable names can contain letters, numbers, and underscores (_).
# 2. Variable names cannot start with a number.
# 3. Variable names are case-sensitive.
# 4. Variable names should not contain spaces.
# 5. Avoid using Python keywords (if, for, while, class, etc.).

# Valid variable names
student_name = "Alice"
age = 25
salary_2025 = 50000
_marks = 90

# Invalid variable names
# 2name = "Bob"          # Starts with a number
# first name = "Alice"   # Contains space
# class = "Python"       # Python keyword

# ==========================================
# Creating Variables
# ==========================================

language = "Python"
version = 3.13
is_easy = True

print(language)
print(version)
print(is_easy)

# ==========================================
# Example 1
# ==========================================

book = "Atomic Habits"
price = 450

print("Book:", book)
print("Price:", price)

# ==========================================
# Example 2
# ==========================================

city = "Hyderabad"
temperature = 32.5

print("City:", city)
print("Temperature:", temperature)

# ==========================================
# Multiple Variable Assignment
# ==========================================

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# Assigning the same value to multiple variables

a = b = c = 100

print(a)
print(b)
print(c)

# ==========================================
# Swapping Variables
# ==========================================

num1 = 5
num2 = 10

print("Before Swapping")
print("num1 =", num1)
print("num2 =", num2)

num1, num2 = num2, num1

print("After Swapping")
print("num1 =", num1)
print("num2 =", num2)

# ==========================================
# Updating Variables
# ==========================================

count = 1

print("Before Update:", count)

count = count + 1

print("After Update:", count)

# ==========================================
# Common Mistakes
# ==========================================

# Wrong
# student name = "Alice"

# Correct
student_name = "Alice"

# Wrong
# 1age = 25

# Correct
age1 = 25

# ==========================================
# Practice Questions
# ==========================================

# 1. Create a variable called company and store "OpenAI".
# 2. Create a variable called experience and store 3.
# 3. Create three variables in one line.
# 4. Swap two variables.
# 5. Update a variable by adding 5 to it.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is a variable?
# Q2. What are the rules for naming variables?
# Q3. What is multiple assignment?
# Q4. How do you swap two variables in Python?
# Q5. Is Python case-sensitive?

# ==========================================
# End of File
# ==========================================