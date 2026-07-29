import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original:")
print(arr)

reshaped = arr.reshape(2, 3)

print("\nReshaped:")
print(reshaped)


arr = np.array([10, 20, 30, 40, 50, 60])

new_arr = arr.reshape(3, 2)

print(new_arr)


arr = np.array([[1, 2],
                [3, 4],
                [5, 6]])

print(arr)

new_arr = arr.reshape(2, 3)

print(new_arr)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr.reshape(2, 4)

arr = np.array([10,20,30,40,50,60])
arr.reshape(3, 2)

arr = np.array([5,10,15,20,25,30,35,40,45])
arr.reshape(3, 3)


arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(2, -1))

arr = np.array([1,2,3,4,5,6])
print(arr.reshape(-1,2))

arr = np.array([10,20,30,40,50,60,70,80])
print(arr.reshape(4,-1))

arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2, -1))

arr = np.array([10,20,30,40,50,60,70,80,90,100,110,120])
print(arr.reshape(-1, 3))


arr = np.arange(1, 9)

print("Original:")
print(arr)

three_d = arr.reshape(2, 2, 2)

print("\n3D Array:")
print(three_d)


arr = np.arange(1, 13)

three_d = arr.reshape(2, 2, 3)

print(three_d)
print(three_d.shape)

arr = np.arange(1, 9)

reshaped = arr.reshape(2, 2, 2)

print(reshaped)

arr = np.arange(1, 13)

reshaped = arr.reshape(2, 2, 3)

print(reshaped)
print(reshaped.shape)