import numpy as np

# ==========================================
# Element-wise Operations
# ==========================================

arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)


# ==========================================
# Python List vs NumPy Array
# ==========================================

list1 = [10, 20, 30]
list2 = [1, 2, 3]

print("Python List Addition:", list1 + list2)


# ==========================================
# Scalar Operations
# ==========================================

arr = np.array([5, 10, 15])

print("Add 10:", arr + 10)
print("Multiply by 3:", arr * 3)
print("Subtract 2:", arr - 2)
print("Divide by 5:", arr / 5)


# ==========================================
# Python List Multiplication
# ==========================================

list1 = [5, 10, 15]

print("Python List * 3:", list1 * 3)


# ==========================================
# Power (**)
# ==========================================

arr = np.array([2, 4, 6])

print("Square:", arr ** 2)


# ==========================================
# Modulus (%)
# ==========================================

print("Modulus:", arr % 4)


# ==========================================
# More Practice
# ==========================================

arr = np.array([3, 5, 8])

print("Cube:", arr ** 3)
print("Modulus:", arr % 5)


# ==========================================
# Scalar Broadcasting Practice
# ==========================================

arr = np.array([3, 6, 9])

print(arr + 2)
print(arr * 5)
print(arr - 1)
print(arr / 3)





























'''
import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

list1 = [10, 20, 30]
list2 = [1, 2, 3]

print(list1 + list2)

arr = np.array([5, 10, 15])
print(arr + 10)
print(arr * 3)
print(arr - 2)
print(arr / 5)

list1 = [5, 10, 15]
print(list1 * 3)


arr = np.array([2, 4, 6])
print(arr ** 2)
print(arr % 4)


arr = np.array([3, 5, 8])
print(arr ** 3)
print(arr % 5)


arr = np.array([3, 6, 9])
print(arr + 2)
print(arr * 5)
print(arr - 1)
print(arr / 3)


arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
b = np.array([1, 2, 3])
print(arr + b)


arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20, 30])
print(arr * b)


marks = np.array([50, 60, 70, 80, 90])
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))


marks = np.array([
    [80, 70, 90],
    [60, 75, 85]
])
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
'''