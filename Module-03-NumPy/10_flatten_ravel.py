import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

flat = arr.flatten()

print("Original:")
print(arr)

print("\nFlatten:")
print(flat)


arr = np.array([[1, 2],
                [3, 4]])

flat = arr.flatten()

flat[0] = 100

print("Flatten Array:")
print(flat)

print("\nOriginal Array:")
print(arr)


arr = np.array([[1, 2],
                [3, 4]])

rav = arr.ravel()

print(rav)


arr = np.array([[1, 2],
                [3, 4]])

rav = arr.ravel()

rav[0] = 100

print("Ravel Array:")
print(rav)

print("\nOriginal Array:")
print(arr)

arr = np.array([[10,20],

                [30,40]])

flat = arr.flatten()

print(flat)

flat = arr.flatten()

flat[1] = 999

print(flat)

print(arr)


flat = arr.flatten()

flat[1] = 999

print(flat)

print(arr)


arr = np.array([[10,20],

                [30,40]])

flat[1] = 999

print(flat)

print(arr)

arr = np.array([[5,10],

                [15,20]])

rav = arr.ravel()

rav[2] = 500

print(rav)

print(arr)