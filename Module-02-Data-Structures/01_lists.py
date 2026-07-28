"""
Module 2 - Lists

Topics Covered:
- Creating Lists
- Indexing
- Negative Indexing
- Slicing
- Updating Elements
- append()
- insert()
- remove()
- pop()
- sort()
- reverse()
- len()
- Membership Operators
"""

# Creating a list
fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits)

# Indexing
print(fruits[0])
print(fruits[-1])

# Slicing
print(fruits[1:3])

# Updating
fruits[1] = "Grapes"
print(fruits)

# append()
fruits.append("Pineapple")
print(fruits)

# insert()
fruits.insert(2, "Kiwi")
print(fruits)

# remove()
fruits.remove("Orange")
print(fruits)

# pop()
fruits.pop()
print(fruits)

# sort()
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)

# reverse()
numbers.reverse()
print(numbers)

# len()
print(len(numbers))

# Membership
print("Apple" in fruits)
print("Watermelon" not in fruits)