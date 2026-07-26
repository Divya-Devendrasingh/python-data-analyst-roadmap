# ==========================================
# Module 1: Python Basics
# Topic: range() Function
# ==========================================

"""
Definition:
The range() function generates a sequence of numbers.
It is commonly used with for loops to repeat a block of
code a specific number of times.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand the range() function.
# 2. Learn different forms of range().
# 3. Use range() with loops.

# ==========================================
# Syntax
# ==========================================

# range(stop)
# range(start, stop)
# range(start, stop, step)

# ==========================================
# Example 1: range(stop)
# ==========================================

print("Example 1")

for number in range(5):
    print(number)

# ==========================================
# Example 2: range(start, stop)
# ==========================================

print("\nExample 2")

for number in range(1, 6):
    print(number)

# ==========================================
# Example 3: range(start, stop, step)
# ==========================================

print("\nExample 3")

for number in range(2, 11, 2):
    print(number)

# ==========================================
# Example 4: Reverse Order
# ==========================================

print("\nExample 4")

for number in range(10, 0, -1):
    print(number)

# ==========================================
# Example 5: Multiplication Table
# ==========================================

print("\nExample 5")

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# ==========================================
# Example 6: Sum of Numbers
# ==========================================

print("\nExample 6")

total = 0

for number in range(1, 11):
    total += number

print(f"Sum = {total}")

# ==========================================
# Example 7: Squares of Numbers
# ==========================================

print("\nExample 7")

for number in range(1, 6):
    print(f"{number}² = {number ** 2}")

# ==========================================
# Practical Example
# ==========================================

print("\nPractical Example")

monthly_sales = [12000, 15000, 18000, 21000]

for month in range(len(monthly_sales)):
    print(f"Month {month + 1}: ₹{monthly_sales[month]}")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# range(1, 5, 0)

# Step value cannot be zero.

print("\nReturn Type")
print(type(range(5)))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use range() for fixed iterations.
# ✔ Use meaningful variable names.
# ✔ Choose an appropriate step value.

# ==========================================
# Practice Questions
# ==========================================

# 1. Print numbers from 1 to 20.
# 2. Print even numbers from 2 to 20.
# 3. Print numbers from 20 to 1.
# 4. Print multiples of 5.
# 5. Find the sum of numbers from 1 to 100.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is range()?
# Q2. What are the three forms of range()?
# Q3. Is the stop value included?
# Q4. Can range() generate numbers in reverse?
# Q5. What is the return type of range()?

# ==========================================
# End of File
# ==========================================