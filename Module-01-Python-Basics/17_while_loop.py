# ==========================================
# Module 1: Python Basics
# Topic: while Loop
# ==========================================

"""
Definition:
A while loop repeatedly executes a block of code as long
as the given condition is True.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand while loops.
# 2. Control repetition using conditions.
# 3. Prevent infinite loops.
# 4. Use while loops in practical examples.

# ==========================================
# Syntax
# ==========================================

# while condition:
#     statement

# ==========================================
# Example 1: Print Numbers
# ==========================================

print("Example 1")

count = 1

while count <= 5:
    print(count)
    count += 1

# ==========================================
# Example 2: Even Numbers
# ==========================================

print("\nExample 2")

number = 2

while number <= 10:
    print(number)
    number += 2

# ==========================================
# Example 3: Countdown
# ==========================================

print("\nExample 3")

count = 5

while count >= 1:
    print(count)
    count -= 1

# ==========================================
# Example 4: Sum of Numbers
# ==========================================

print("\nExample 4")

count = 1
total = 0

while count <= 5:
    total += count
    count += 1

print(f"Sum = {total}")

# ==========================================
# Example 5: Multiplication Table
# ==========================================

print("\nExample 5")

number = 5
i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# ==========================================
# Example 6: Login Attempts
# ==========================================

print("\nExample 6")

attempt = 1

while attempt <= 3:
    print(f"Login Attempt {attempt}")
    attempt += 1

# ==========================================
# Practical Example
# ==========================================

print("\nPractical Example")

balance = 5000

while balance > 0:
    print(f"Remaining Balance: ₹{balance}")
    balance -= 1000

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# count = 1
# while count <= 5:
#     print(count)

# Infinite loop because count is never updated.

print("\nReturn Type")
print(type(count <= 5))

# ==========================================
# Best Practices
# ==========================================

# ✔ Always update the loop variable.
# ✔ Avoid infinite loops.
# ✔ Use meaningful variable names.

# ==========================================
# Practice Questions
# ==========================================

# 1. Print numbers from 1 to 20.
# 2. Print even numbers using while.
# 3. Print numbers in reverse order.
# 4. Find the sum of the first 10 numbers.
# 5. Print the multiplication table of any number.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is a while loop?
# Q2. What is an infinite loop?
# Q3. When should you use a while loop?
# Q4. What is the difference between for and while?
# Q5. How do you stop a while loop?

# ==========================================
# End of File
# ==========================================