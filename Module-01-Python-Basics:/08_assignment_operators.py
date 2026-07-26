# ==========================================
# Module 1: Python Basics
# Topic: Assignment Operators
# ==========================================

"""
Definition:
Assignment operators are used to assign values to variables.
They can also perform an operation and assign the result
back to the same variable.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand assignment operators.
# 2. Learn shorthand assignment.
# 3. Perform calculations using assignment operators.

# ==========================================
# Assignment Operator (=)
# ==========================================

x = 10

print("Assignment Operator (=)")
print(f"x = {x}")

# ==========================================
# Addition Assignment (+=)
# ==========================================

x = 10
x += 5

print("\nAddition Assignment (+=)")
print(f"x += 5 → {x}")

# ==========================================
# Subtraction Assignment (-=)
# ==========================================

x = 10
x -= 3

print("\nSubtraction Assignment (-=)")
print(f"x -= 3 → {x}")

# ==========================================
# Multiplication Assignment (*=)
# ==========================================

x = 10
x *= 4

print("\nMultiplication Assignment (*=)")
print(f"x *= 4 → {x}")

# ==========================================
# Division Assignment (/=)
# ==========================================

x = 20
x /= 4

print("\nDivision Assignment (/=)")
print(f"x /= 4 → {x}")

# ==========================================
# Floor Division Assignment (//=)
# ==========================================

x = 25
x //= 4

print("\nFloor Division Assignment (//=)")
print(f"x //= 4 → {x}")

# ==========================================
# Modulus Assignment (%=)
# ==========================================

x = 25
x %= 4

print("\nModulus Assignment (%=)")
print(f"x %= 4 → {x}")

# ==========================================
# Exponent Assignment (**=)
# ==========================================

x = 3
x **= 3

print("\nExponent Assignment (**=)")
print(f"x **= 3 → {x}")

# ==========================================
# Practical Example
# ==========================================

balance = 5000

print("\nPractical Example")

balance += 1500
print(f"After Deposit: ₹{balance}")

balance -= 800
print(f"After Purchase: ₹{balance}")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# x =+ 5

# Correct:
# x += 5

print("\nReturn Type")
print(type(balance))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use shorthand assignment whenever appropriate.
# ✔ Use meaningful variable names.
# ✔ Improve readability with assignment operators.

# ==========================================
# Practice Questions
# ==========================================

# 1. Increase a number using +=.
# 2. Decrease a number using -=.
# 3. Double a number using *=.
# 4. Divide a number using /=.
# 5. Find the remainder using %=.
# 6. Find the square using **=.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What are assignment operators?
# Q2. What is the difference between = and +=?
# Q3. What does %= do?
# Q4. What is the purpose of **=?
# Q5. Why are assignment operators useful?

# ==========================================
# End of File
# ==========================================