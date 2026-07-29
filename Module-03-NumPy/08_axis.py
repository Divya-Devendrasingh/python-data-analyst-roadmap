import numpy as np

# ==========================================
# Axis Example
# ==========================================

marks = np.array([
    [80, 70, 90],
    [60, 75, 85]
])

print("Array:")
print(marks)

print("\nSum of all elements:")
print(np.sum(marks))

print("\nSum column-wise (axis=0):")
print(np.sum(marks, axis=0))

print("\nSum row-wise (axis=1):")
print(np.sum(marks, axis=1))



arr = np.array([
    [5, 10],
    [15, 20]
])

print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

marks = np.array([
    [80, 70, 90],
    [60, 75, 85]
])

print(np.mean(marks))
print(np.mean(marks, axis=0))
print(np.mean(marks, axis=1))

arr = np.array([
    [10, 20],
    [30, 40]
])

print(np.mean(arr))
print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))


arr = np.array([
    [10, 20],
    [30, 40]
])

print("Maximum of all elements:")
print(np.max(arr))

print("\nColumn-wise Maximum (axis=0):")
print(np.max(arr, axis=0))

print("\nRow-wise Maximum (axis=1):")
print(np.max(arr, axis=1))

print("\nMinimum of all elements:")
print(np.min(arr))

print("\nColumn-wise Minimum (axis=0):")
print(np.min(arr, axis=0))

print("\nRow-wise Minimum (axis=1):")
print(np.min(arr, axis=1))

arr = np.array([
    [8, 3, 6],
    [5, 9, 1]
])

print(np.max(arr))
print(np.max(arr, axis=0))
print(np.max(arr, axis=1))

print(np.min(arr))
print(np.min(arr, axis=0))
print(np.min(arr, axis=1))