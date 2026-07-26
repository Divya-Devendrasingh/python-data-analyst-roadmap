# ==========================================
# Module 1: Python Basics
# Topic: Arithmetic Operators
# ==========================================

"""
Definition:
Arithmetic operators are used to perform mathematical operations on numbers.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand arithmetic operators.
# 2. Perform mathematical calculations.
# 3. Learn operator precedence.

# ==========================================
# Addition (+)
# ==========================================

a = 20
b = 10

print("Addition")
print(f"{a} + {b} = {a + b}")

# ==========================================
# Subtraction (-)
# ==========================================

print("\nSubtraction")
print(f"{a} - {b} = {a - b}")

# ==========================================
# Multiplication (*)
# ==========================================

print("\nMultiplication")
print(f"{a} * {b} = {a * b}")

# ==========================================
# Division (/)
# ==========================================

print("\nDivision")
print(f"{a} / {b} = {a / b}")

# ==========================================
# Floor Division (//)
# ==========================================

print("\nFloor Division")
print(f"{21} // {4} = {21 // 4}")

# ==========================================
# Modulus (%)
# ==========================================

print("\nModulus")
print(f"{21} % {4} = {21 % 4}")

# ==========================================
# Exponent (**)
# ==========================================

print("\nExponent")
print(f"{2} ** {5} = {2 ** 5}")

# ==========================================
# Operator Precedence
# ==========================================

print("\nOperator Precedence")

print(f"10 + 5 * 2 = {10 + 5 * 2}")
print(f"(10 + 5) * 2 = {(10 + 5) * 2}")

# ==========================================
# Practical Example
# ==========================================

price = 450
quantity = 3

total_amount = price * quantity

print("\nPractical Example")
print(f"Price: ₹{price}")
print(f"Quantity: {quantity}")
print(f"Total Amount: ₹{total_amount}")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# print(10 / 2 == 5)

# Note:
# Division (/) always returns a float.

print("\nDivision Returns Float")
print(type(10 / 2))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use meaningful variable names.
# ✔ Use parentheses to improve readability.
# ✔ Remember that / always returns float.

# ==========================================
# Practice Questions
# ==========================================

# 1. Add two numbers.
# 2. Find the difference between two numbers.
# 3. Multiply two numbers.
# 4. Divide two numbers.
# 5. Find the remainder using %.
# 6. Find the square of a number using **.
# 7. Write an expression using parentheses.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What are arithmetic operators?
# Q2. What is the difference between / and //?
# Q3. What does % return?
# Q4. What does ** do?
# Q5. Explain operator precedence in Python.

# ==========================================
# End of File
# ==========================================