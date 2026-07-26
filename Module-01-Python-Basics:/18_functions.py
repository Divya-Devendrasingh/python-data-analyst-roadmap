# ==========================================
# Module 1: Python Basics
# Topic: Functions
# ==========================================

"""
Definition:
A function is a reusable block of code that performs a
specific task. Functions help reduce code duplication
and improve readability.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand functions.
# 2. Define and call functions.
# 3. Improve code reusability.
# 4. Organize programs using functions.

# ==========================================
# Syntax
# ==========================================

# def function_name():
#     statements
#
# function_name()

# ==========================================
# Example 1: Simple Function
# ==========================================

def greet():
    print("Hello, Python!")


print("Example 1")
greet()

# ==========================================
# Example 2: Function Called Multiple Times
# ==========================================

def welcome():
    print("Welcome to Python Programming")


print("\nExample 2")
welcome()
welcome()
welcome()

# ==========================================
# Example 3: Function with Local Variable
# ==========================================

def display_course():
    course = "Python"
    print(f"Course: {course}")


print("\nExample 3")
display_course()

# ==========================================
# Example 4: Function Performing Calculation
# ==========================================

def add_numbers():
    a = 10
    b = 20
    print(f"Sum = {a + b}")


print("\nExample 4")
add_numbers()

# ==========================================
# Example 5: Function Returning Nothing
# ==========================================

def show_message():
    print("Learning Functions")


print("\nExample 5")
show_message()

# ==========================================
# Example 6: Multiple Functions
# ==========================================

def python():
    print("Python")


def sql():
    print("SQL")


def power_bi():
    print("Power BI")


print("\nExample 6")
python()
sql()
power_bi()

# ==========================================
# Practical Example
# ==========================================

def monthly_report():
    sales = 150000
    expenses = 90000
    profit = sales - expenses

    print("\nMonthly Report")
    print(f"Sales     : ₹{sales}")
    print(f"Expenses  : ₹{expenses}")
    print(f"Profit    : ₹{profit}")


monthly_report()

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# greet

# Correct:
# greet()

print("\nFunction Type")
print(type(greet))

# ==========================================
# Best Practices
# ==========================================

# ✔ Give functions meaningful names.
# ✔ Keep functions short and focused.
# ✔ Reuse functions whenever possible.

# ==========================================
# Practice Questions
# ==========================================

# 1. Create a function to print your favorite programming language.
# 2. Create a function to print numbers from 1 to 5.
# 3. Create a function that prints a welcome message.
# 4. Create a function to calculate the square of a number.
# 5. Call the same function three times.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is a function?
# Q2. Why do we use functions?
# Q3. What is the difference between defining and calling a function?
# Q4. Can a function be called multiple times?
# Q5. What happens if you forget parentheses while calling a function?

# ==========================================
# End of File
# ==========================================