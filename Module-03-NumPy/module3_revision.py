"""
=========================================
Module 3 Revision - NumPy
Python Data Analyst Roadmap
=========================================

Topics Covered
--------------
1. Creating Arrays
2. Array Attributes
3. Indexing & Slicing
4. Array Operations
5. Broadcasting
6. Aggregation Functions
7. Axis
8. Reshape
9. Flatten & Ravel
10. Boolean Indexing
11. Filtering
12. Random Module
13. Stacking & Splitting
14. Useful Functions

"""

import numpy as np

print("=" * 50)
print("MODULE 3 - NUMPY REVISION")
print("=" * 50)

# -------------------------------------
# Question 1 - Indexing & Slicing
# -------------------------------------

print("\nQuestion 1")

arr = np.array([10, 20, 30, 40, 50])

print("First Element :", arr[0])
print("Last Element  :", arr[-1])
print("Middle Elements :", arr[1:4])

# -------------------------------------
# Question 2 - Array Operations
# -------------------------------------

print("\nQuestion 2")

arr = np.array([5, 10, 15, 20, 25])

print(arr * 3)

# -------------------------------------
# Question 3 - Random + Aggregation
# -------------------------------------

print("\nQuestion 3")

marks = np.random.randint(35, 101, size=10)

print("Marks :", marks)
print("Highest :", np.max(marks))
print("Lowest :", np.min(marks))
print("Average :", np.mean(marks))

# -------------------------------------
# Question 4 - Boolean Indexing
# -------------------------------------

print("\nQuestion 4")

marks = np.array([95, 45, 80, 30, 70])

print("Passed Students :", marks[marks >= 50])

# -------------------------------------
# Question 5 - Stacking
# -------------------------------------

print("\nQuestion 5")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vertical Stack")
print(np.vstack((a, b)))

print("\nHorizontal Stack")
print(np.hstack((a, b)))

print("\nRevision Completed Successfully!")