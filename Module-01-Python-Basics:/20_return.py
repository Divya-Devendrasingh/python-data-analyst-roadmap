# ==========================================
# Module 1: Python Basics
# Topic: Return Statement
# ==========================================

"""
Definition:
The return statement is used to send a value back from a
function to the place where the function was called.

Unlike print(), return allows the returned value to be
stored in a variable, reused, or passed to another function.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand the return statement.
# 2. Learn the difference between print() and return.
# 3. Return single and multiple values.
# 4. Store returned values in variables.

# ==========================================
# Syntax
# ==========================================

# def function_name():
#     return value

# ==========================================
# Example 1: Return a Number
# ==========================================

def get_number():
    return 100


print("Example 1")
print(get_number())

# ==========================================
# Example 2: Return Addition
# ==========================================

def add_numbers(a, b):
    return a + b


print("\nExample 2")
result = add_numbers(20, 30)
print(f"Sum = {result}")

# ==========================================
# Example 3: Return a String
# ==========================================

def get_message():
    return "Welcome to Python"


print("\nExample 3")
message = get_message()
print(message)

# ==========================================
# Example 4: Return Boolean
# ==========================================

def is_adult(age):
    return age >= 18


print("\nExample 4")
print(is_adult(25))
print(is_adult(15))

# ==========================================
# Example 5: Return Multiple Values
# ==========================================

def student_details():
    return "Alice", 24, "Delhi"


print("\nExample 5")

name, age, city = student_details()

print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")

# ==========================================
# Example 6: Return Calculation
# ==========================================

def calculate_area(length, width):
    return length * width


print("\nExample 6")

area = calculate_area(10, 5)

print(f"Area = {area}")

# ==========================================
# Practical Example
# ==========================================

def calculate_profit(sales, expenses):
    return sales - expenses


print("\nPractical Example")

sales = 150000
expenses = 90000

profit = calculate_profit(sales, expenses)

print(f"Sales     : ₹{sales}")
print(f"Expenses  : ₹{expenses}")
print(f"Profit    : ₹{profit}")

# ==========================================
# Difference Between print() and return
# ==========================================

def print_message():
    print("Hello from print()")


def return_message():
    return "Hello from return()"


print("\nDifference Between print() and return")

print_message()

returned_value = return_message()

print(returned_value)

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# print(add_numbers)

# Correct:
# print(add_numbers(10, 20))

print("\nFunction Type")
print(type(add_numbers))

# ==========================================
# Best Practices
# ==========================================

# ✔ Return values instead of printing whenever possible.
# ✔ Keep functions focused on one task.
# ✔ Use meaningful function names.

# ==========================================
# Practice Questions
# ==========================================

# 1. Create a function that returns the square of a number.
# 2. Create a function that returns the larger of two numbers.
# 3. Create a function that returns the average of three numbers.
# 4. Create a function that returns a greeting message.
# 5. Create a function that returns True if a number is even.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is the purpose of the return statement?
# Q2. What is the difference between print() and return?
# Q3. Can a function return multiple values?
# Q4. What happens if a function has no return statement?
# Q5. Why is return preferred in reusable functions?

# ==========================================
# End of File
# ==========================================