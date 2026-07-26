# ==========================================
# Module 1: Python Basics
# Topic: for Loop
# ==========================================

"""
Definition:
A for loop is used to iterate over a sequence such as a
string, list, tuple, set, dictionary, or range.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand for loops.
# 2. Iterate through sequences.
# 3. Use range().
# 4. Perform repetitive tasks.

# ==========================================
# Syntax
# ==========================================

# for variable in sequence:
#     statement

# ==========================================
# Example 1: Loop Through a List
# ==========================================

languages = ["Python", "SQL", "Power BI", "Excel"]

print("Example 1")

for language in languages:
    print(language)

# ==========================================
# Example 2: Loop Through a String
# ==========================================

word = "Python"

print("\nExample 2")

for character in word:
    print(character)

# ==========================================
# Example 3: Using range()
# ==========================================

print("\nExample 3")

for number in range(1, 6):
    print(number)

# ==========================================
# Example 4: Using range(start, stop, step)
# ==========================================

print("\nExample 4")

for number in range(2, 11, 2):
    print(number)

# ==========================================
# Example 5: Calculate Total
# ==========================================

prices = [100, 200, 300]

total = 0

print("\nExample 5")

for price in prices:
    total += price

print(f"Total Price: ₹{total}")

# ==========================================
# Example 6: Dictionary Iteration
# ==========================================

student = {
    "Name": "Alice",
    "Age": 24,
    "City": "Delhi"
}

print("\nExample 6")

for key, value in student.items():
    print(f"{key}: {value}")

# ==========================================
# Example 7: Multiplication Table
# ==========================================

number = 5

print("\nExample 7")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# ==========================================
# Practical Example
# ==========================================

sales = [15000, 22000, 18000, 25000]

print("\nPractical Example")

total_sales = 0

for sale in sales:
    total_sales += sale

print(f"Total Sales: ₹{total_sales}")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# for i range(5):

# Correct:
# for i in range(5):
#     print(i)

print("\nReturn Type")
print(type(range(5)))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use meaningful loop variable names.
# ✔ Avoid unnecessary nested loops.
# ✔ Keep loop logic simple and readable.

# ==========================================
# Practice Questions
# ==========================================

# 1. Print numbers from 1 to 10.
# 2. Print even numbers from 2 to 20.
# 3. Print each character of a string.
# 4. Find the sum of a list.
# 5. Print the multiplication table of any number.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is a for loop?
# Q2. When do you use a for loop?
# Q3. What does range() return?
# Q4. Can a for loop iterate over a dictionary?
# Q5. What is the difference between a for loop and a while loop?

# ==========================================
# End of File
# ==========================================