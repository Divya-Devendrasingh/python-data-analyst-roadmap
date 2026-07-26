# ==========================================
# Module 1: Python Basics
# Topic: Input
# ==========================================

"""
Definition:
The input() function is used to accept input from the user during program execution.

Note:
By default, input() always returns a string (str).
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Learn how to take input from the user.
# 2. Understand that input() returns a string.
# 3. Learn type conversion using int() and float().
# 4. Take multiple inputs.

# ==========================================
# Syntax
# ==========================================

# variable_name = input("Enter a value: ")

# ==========================================
# Example 1: String Input
# ==========================================

name = input("Enter your name: ")

print("Hello,", name)

# ==========================================
# Example 2: Integer Input
# ==========================================

age = int(input("\nEnter your age: "))

print("Age:", age)
print("Next year your age will be:", age + 1)

# ==========================================
# Example 3: Float Input
# ==========================================

height = float(input("\nEnter your height (in meters): "))

print("Height:", height)

# ==========================================
# Example 4: Multiple Inputs
# ==========================================

city = input("\nEnter your city: ")
country = input("Enter your country: ")

print("City:", city)
print("Country:", country)

# ==========================================
# Example 5: Two Numbers
# ==========================================

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)

# ==========================================
# Understanding input()
# ==========================================

number = input("\nEnter any number: ")

print("Value:", number)
print("Data Type:", type(number))

# ==========================================
# Common Mistakes
# ==========================================

# Wrong
# age = input("Enter age: ")
# print(age + 5)

# Correct
age = int(input("\nEnter your age again: "))
print("Age after 5 years:", age + 5)

# ==========================================
# Best Practices
# ==========================================

# ✔ Use meaningful prompt messages.
# ✔ Convert input to int or float when performing calculations.
# ✔ Validate user input in real-world applications.

# ==========================================
# Practice Questions
# ==========================================

# 1. Take your favorite color as input and print it.
# 2. Take two integers and print their product.
# 3. Take your weight as float input and print it.
# 4. Take your first name and last name separately and print the full name.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What does input() do?
# Q2. What data type does input() return?
# Q3. Why do we use int(input())?
# Q4. What happens if you don't convert input before doing arithmetic?
# Q5. How do you take float input from the user?

# ==========================================
# End of File
# ==========================================