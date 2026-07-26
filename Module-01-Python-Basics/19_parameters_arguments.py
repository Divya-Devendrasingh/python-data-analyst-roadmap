# ==========================================
# Module 1: Python Basics
# Topic: Parameters and Arguments
# ==========================================

"""
Definition:
A parameter is a variable defined in a function.
An argument is the actual value passed to the function
when it is called.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand parameters and arguments.
# 2. Pass values to functions.
# 3. Use multiple parameters.
# 4. Learn default parameters.
# 5. Use keyword arguments.

# ==========================================
# Syntax
# ==========================================

# def function_name(parameter):
#     statements
#
# function_name(argument)

# ==========================================
# Example 1: One Parameter
# ==========================================

def greet(name):
    print(f"Hello, {name}!")


print("Example 1")
greet("Alice")

# ==========================================
# Example 2: Two Parameters
# ==========================================

def add_numbers(a, b):
    print(f"{a} + {b} = {a + b}")


print("\nExample 2")
add_numbers(10, 20)

# ==========================================
# Example 3: Multiple Parameters
# ==========================================

def student_details(name, age, city):
    print(f"Name : {name}")
    print(f"Age  : {age}")
    print(f"City : {city}")


print("\nExample 3")
student_details("Alice", 24, "Delhi")

# ==========================================
# Example 4: Default Parameter
# ==========================================

def greet_user(name="Guest"):
    print(f"Welcome, {name}!")


print("\nExample 4")
greet_user()
greet_user("Bob")

# ==========================================
# Example 5: Keyword Arguments
# ==========================================

def employee(name, department, salary):
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Salary     : ₹{salary}")


print("\nExample 5")
employee(
    department="Data Analytics",
    salary=60000,
    name="Alice"
)

# ==========================================
# Example 6: Positional Arguments
# ==========================================

def multiply(a, b):
    print(f"{a} × {b} = {a * b}")


print("\nExample 6")
multiply(6, 8)

# ==========================================
# Practical Example
# ==========================================

def calculate_profit(sales, expenses):
    profit = sales - expenses

    print("\nPractical Example")
    print(f"Sales     : ₹{sales}")
    print(f"Expenses  : ₹{expenses}")
    print(f"Profit    : ₹{profit}")


calculate_profit(150000, 90000)

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# greet()

# Correct:
# greet("Alice")

print("\nFunction Type")
print(type(greet))

# ==========================================
# Best Practices
# ==========================================

# ✔ Use meaningful parameter names.
# ✔ Keep the number of parameters reasonable.
# ✔ Use default values when appropriate.
# ✔ Use keyword arguments for better readability.

# ==========================================
# Practice Questions
# ==========================================

# 1. Create a function that accepts your name.
# 2. Create a function that adds two numbers.
# 3. Create a function that calculates the area of a rectangle.
# 4. Create a function with a default parameter.
# 5. Call a function using keyword arguments.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is the difference between a parameter and an argument?
# Q2. What are positional arguments?
# Q3. What are keyword arguments?
# Q4. What is a default parameter?
# Q5. Why are parameters useful in functions?

# ==========================================
# End of File
# ==========================================