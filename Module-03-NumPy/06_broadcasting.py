import numpy as np

# ==========================================
# Broadcasting Example 1
# ==========================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2, 3])

print("Original Array:")
print(arr)

print("\nBroadcast Array:")
print(b)

print("\nAddition Result:")
print(arr + b)


# ==========================================
# Broadcasting Example 2
# ==========================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print("\nOriginal Array:")
print(arr)

print("\nBroadcast Array:")
print(b)

print("\nMultiplication Result:")
print(arr * b)


# ==========================================
# Broadcasting Failure Example
# ==========================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

b = np.array([1, 2])

print("\nBroadcast Failure Example")

try:
    print(arr + b)
except ValueError as e:
    print("Error:", e)