# ==========================================
# Module 1: Python Basics
# Topic: Nested if Statement
# ==========================================

"""
Definition:
A nested if statement is an if statement inside another
if statement. It is used when one condition depends on
another condition.
"""

# ==========================================
# Learning Objectives
# ==========================================

# 1. Understand nested if statements.
# 2. Write dependent conditions.
# 3. Build decision-making programs.

# ==========================================
# Syntax
# ==========================================

# if condition1:
#     if condition2:
#         statement

# ==========================================
# Example 1: Voting Eligibility
# ==========================================

age = 22
citizen = True

print("Example 1")

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Citizenship Required")
else:
    print("Not Eligible")

# ==========================================
# Example 2: Student Result
# ==========================================

marks = 85
attendance = 90

print("\nExample 2")

if marks >= 40:
    if attendance >= 75:
        print("Pass")
    else:
        print("Attendance Shortage")
else:
    print("Fail")

# ==========================================
# Example 3: Login Verification
# ==========================================

username = "admin"
password = "python123"

print("\nExample 3")

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

# ==========================================
# Example 4: Loan Eligibility
# ==========================================

salary = 65000
experience = 3

print("\nExample 4")

if salary >= 50000:
    if experience >= 2:
        print("Loan Approved")
    else:
        print("Insufficient Experience")
else:
    print("Salary Requirement Not Met")

# ==========================================
# Example 5: Product Discount
# ==========================================

purchase_amount = 6000
premium_member = True

print("\nExample 5")

if purchase_amount >= 5000:
    if premium_member:
        print("20% Discount")
    else:
        print("10% Discount")
else:
    print("No Discount")

# ==========================================
# Practical Example
# ==========================================

balance = 10000
upi_pin_verified = True

print("\nPractical Example")

if balance >= 500:
    if upi_pin_verified:
        print("Transaction Successful")
    else:
        print("PIN Verification Failed")
else:
    print("Insufficient Balance")

# ==========================================
# Common Mistakes
# ==========================================

# Wrong:
# if age >= 18:
# print("Eligible")

# Correct:
# if age >= 18:
#     if citizen:
#         print("Eligible")

print("\nReturn Type")
print(type(age >= 18))

# ==========================================
# Best Practices
# ==========================================

# ✔ Avoid excessive nesting.
# ✔ Use meaningful conditions.
# ✔ Maintain proper indentation.
# ✔ Consider using logical operators if nesting becomes deep.

# ==========================================
# Practice Questions
# ==========================================

# 1. Check voting eligibility using age and citizenship.
# 2. Check pass/fail using marks and attendance.
# 3. Verify username and password.
# 4. Check loan eligibility.
# 5. Apply discounts based on purchase amount and membership.

# ==========================================
# Interview Questions
# ==========================================

# Q1. What is a nested if statement?
# Q2. When should nested if statements be used?
# Q3. What is the disadvantage of deep nesting?
# Q4. How can logical operators reduce nesting?
# Q5. Where are nested if statements used in real-world applications?

# ==========================================
# End of File
# ==========================================