import numpy as np

jan = np.array([1200,1500,1800])
feb = np.array([1400,1600,1700])

sales = np.vstack((jan, feb))

print(sales)

sales = np.hstack((jan, feb))
print(sales)

arr = np.array([10,20,30,40,50,60])
parts = np.split(arr, 3)
print(parts)

arr = np.array([1,2,3,4,5,6])
parts = np.split(arr, 2)
print(parts)

jan = np.array([120,150,180])
feb = np.array([140,160,170])
mar = np.array([190,210,230])
sales = np.vstack((jan, feb, mar))

a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.vstack((a, b)))
print(np.hstack((a, b)))

arr = np.array([100,200,300,400,500,600]) 
print(np.split(arr, 3))