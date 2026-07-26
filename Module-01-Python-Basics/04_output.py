# ==========================================
# Module 1: Python Basics
# Topic: Output
# ==========================================

"""
Definition:
The print() function is used to display output on the screen.

It is one of the most commonly used functions in Python.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Learn how to display output using print().
# 2. Print multiple values.
# 3. Use the sep parameter.
# 4. Use the end parameter.
# 5. Learn escape characters.
# 6. Learn formatted strings (f-strings).

# ==========================================
# Syntax
# ==========================================

# print(value)

# ==========================================
# Example 1: Basic Output
# ==========================================

print("Hello, Python!")
print("Welcome to Python Basics")

# ==========================================
# Example 2: Printing Multiple Values
# ==========================================

name = "Alice"
age = 25

print("\nPrinting Multiple Values")
print(name, age)

# ==========================================
# Example 3: sep Parameter
# ==========================================

print("\nUsing sep Parameter")
print("Python", "SQL", "Power BI", sep=" | ")

# ==========================================
# Example 4: end Parameter
# ==========================================

print("\nUsing end Parameter")
print("Hello", end=" ")
print("World!")

# ==========================================
# Example 5: Escape Characters
# ==========================================

print("\nEscape Characters")

print("Line 1\nLine 2")
print("Python\tSQL\tPower BI")
print("She said, \"Python is easy!\"")

# ==========================================
# Example 6: f-Strings (Recommended)
# ==========================================

student = "Alice"
marks = 92

print("\nUsing f-Strings")
print(f"Student Name: {student}")
print(f"Marks: {marks}")

# ==========================================
# Example 7: Combining Variables
# ==========================================

city = "Hyderabad"
country = "India"

print("\nLocation")
print(f"{city}, {country}")

# ==========================================
# Example 8: Printing Calculations
# ==========================================

a = 10
b = 20

print("\nCalculations")
print("Addition:", a + b)
print(f"Multiplication: {a * b}")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong
# print("Age: " + 25)

# Correct
print("\nCorrect Example")
print("Age:", 25)

# Or
print(f"Age: {25}")

# ==========================================
# Best Practices
# ==========================================

# ✔ Use f-strings for readable code.
# ✔ Use meaningful output messages.
# ✔ Use sep and end only when needed.

# ==========================================
# Practice Questions
# ==========================================

# 1. Print your favorite programming language.
# 2. Print your name and age together.
# 3. Print three words separated by "-".
# 4. Print two lines using \n.
# 5. Print a sentence using an f-string.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What does print() do?
# Q2. What is the purpose of the sep parameter?
# Q3. What is the purpose of the end parameter?
# Q4. What are escape characters?
# Q5. Why are f-strings preferred over string concatenation?

# ==========================================
# End of File
# ==========================================