"""
Module 2 Revision
"""

# Lists
numbers = [10, 20, 30, 40]

print(numbers)
print(numbers[1])
print(numbers[-1])

numbers.append(50)
numbers.remove(20)

print(numbers)

# Tuples
colors = ("Red", "Green", "Blue")

print(colors.count("Red"))

# Sets
items = {1, 2, 3}

items.add(4)

print(items)

# Dictionaries
employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 50000
}

employee["salary"] = 60000

print(employee)

print(employee.keys())

print(employee.values())