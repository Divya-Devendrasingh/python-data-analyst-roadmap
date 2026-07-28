import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])
print("Second last:", arr[-2])

print("Slice 1:", arr[1:4])
print("Slice 2:", arr[:3])
print("Slice 3:", arr[2:])

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:5])
print(arr[:])
print(arr[:-1])
print(arr[-3:])
print(arr[2])
print(arr[2:3])
print(arr[3])
print(arr[3:4])


arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr)
print(arr[0, 1])
print(arr[2, 0])
print(arr[1, 2])
print(arr[0, 2])
print(arr[2, 2])
print(arr[1, 0])
print(arr[-1, -1])
print(arr[-1, 0])
print(arr[0, -1])
print(arr[-2, -2])
print(arr[:, 1])
print(arr[1, :])
print(arr[0:2, 1:3])
print(arr[:, 0:2])
print(arr[1:, 1:])
print(arr[:2, :2])