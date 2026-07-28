"""
Module 2 - Tuples

Topics Covered:
- Creating Tuples
- Indexing
- Negative Indexing
- Immutability
- count()
- index()
- len()
"""

colors = ("Red", "Blue", "Green", "Blue")

print(colors)

# Indexing
print(colors[0])
print(colors[-1])

# count()
print(colors.count("Blue"))

# index()
print(colors.index("Green"))

# len()
print(len(colors))

# Single element tuple
number = (10,)
print(number)