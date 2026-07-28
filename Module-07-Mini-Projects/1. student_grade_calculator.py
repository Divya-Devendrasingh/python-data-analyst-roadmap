# ==============================================
# Module 1: Python Basics
# Topic: Mini Project - Student Grade Calculator
# ==============================================

name = input("Enter your name: ")

python_marks = int(input("Enter your mark in Python: "))
sql_marks = int(input("Enter your mark in SQL: "))
excel_marks = int(input("Enter your mark in Excel: "))
statistics_marks = int(input("Enter your mark in Statistics: "))
power_bi_marks = int(input("Enter your mark in Power BI: "))

# Calculate total, percentage, and average
total_marks = (
    python_marks +
    sql_marks +
    excel_marks +
    statistics_marks +
    power_bi_marks
)

percentage = (total_marks / 500) * 100
average_marks = total_marks / 5

# Check pass/fail first
if (
    python_marks < 35 or
    sql_marks < 35 or
    excel_marks < 35 or
    statistics_marks < 35 or
    power_bi_marks < 35
):
    grade = "F"
    result = "FAIL"

else:
    result = "PASS"

    if 90 <= percentage <= 100:
        grade = "A+"
    elif 80 <= percentage < 90:
        grade = "A"
    elif 70 <= percentage < 80:
        grade = "B"
    elif 60 <= percentage < 70:
        grade = "C"
    elif 50 <= percentage < 60:
        grade = "D"
    else:
        grade = "F"

# Display Report
print("\n==========================")
print("      REPORT CARD")
print("==========================")

print(f"Name        : {name}")
print(f"Python      : {python_marks}")
print(f"SQL         : {sql_marks}")
print(f"Excel       : {excel_marks}")
print(f"Statistics  : {statistics_marks}")
print(f"Power BI    : {power_bi_marks}")

print("--------------------------")

print(f"Total       : {total_marks}")
print(f"Average     : {average_marks:.2f}")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")
print(f"Result      : {result}")

print("==========================")
