"""
Module 2 - Sets

Topics Covered:
- Creating Sets
- Unique Elements
- add()
- remove()
- discard()
- pop()
- clear()
- len()
"""

numbers = {1, 2, 3, 4, 5}

print(numbers)

numbers.add(6)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.discard(10)
print(numbers)

numbers.pop()
print(numbers)

print(len(numbers))

print(2 in numbers)

numbers.clear()

print(numbers)