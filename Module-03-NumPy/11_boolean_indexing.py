import numpy as np

marks = np.array([35, 78, 91, 45, 60])

passed = marks[marks >= 50]

print(passed)

salary = np.array([30000, 55000, 80000, 45000, 90000])
print(salary[salary > 50000])

price = np.array([80, 150, 60, 200, 90])
print(price[price < 100])

numbers = np.array([1,2,3,4,5,6,7,8])
print(numbers[numbers % 2 == 0])

marks = np.array([25,40,55,70,85])
result = marks[marks>=50]
print(result)

salary = np.array([25000,40000,60000,80000,45000])
print(salary[salary>50000])

numbers = np.array([10,15,20,25,30,35])
even = numbers[numbers%2==0]
print("Even Numbers:", even)

marks = np.array([35, 55, 72, 81, 95])
result = marks[(marks >= 50) & (marks <= 80)]
print(result)

price = np.array([80, 120, 250, 600, 90])
print(price[(price < 100) | (price > 500)])

marks = np.array([35, 78, 91, 45, 60])
print(marks[~(marks >= 50)])

marks = np.array([35,50,65,75,90])
result = marks[(marks >= 50) & (marks <= 80)]
print(result)

price = np.array([50,120,300,700,80])
result = price[(price < 100) | (price >500)]
print(result)

salary = np.array([25000,45000,60000,75000])
result = salary[~(salary>50000)]
print(result)