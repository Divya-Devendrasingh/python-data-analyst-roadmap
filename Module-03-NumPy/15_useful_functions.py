import numpy as np

print(np.arange(1, 11))

print(np.arange(0, 21, 5))

print(np.arange(10, 51, 10))

print(np.linspace(0, 10, 5))

print(np.linspace(0, 100, 6))

print(np.zeros(5))

print(np.ones(4))

print(np.eye(3))

print(np.eye(2))

arr = np.array([10,20,20,30,30,40])
print(np.unique(arr))

arr = np.array([5,2,2,8,8,1,5])
print(np.unique(arr))

arr = np.array([40,10,50,20])
print(np.sort(arr))

arr = np.array([25,10,45,5,30])
print(np.sort(arr))

marks = np.array([95,45,80,32])
result = np.where(marks >= 50, "Pass", "Fail")
print(result)

marks = np.array([35,80,90,45,60])
print(np.where(marks >= 50, "Pass", "Fail"))

arr = np.array([10,40,70,120])
print(np.clip(arr, 20, 100))

arr = np.array([5,25,60,90,100])
print(np.clip(arr, 20,80))


