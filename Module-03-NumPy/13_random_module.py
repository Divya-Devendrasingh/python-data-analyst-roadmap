import numpy as np

marks = np.array([78, 65, 90, 55, 88])

print(marks)

numbers = np.random.randint(1, 11, size=5)
print(numbers)

marks = np.random.randint(35, 101, size=10)
print(marks)

salary = np.random.randint(30000, 80001, size=8)
print(salary)

print(np.random.rand(5))

np.random.seed(42)
print(np.random.randint(1, 11, size=5))

salaries = np.random.randint(40000, 90001, 5)
print(salaries)

np.random.seed(100)
print(np.random.randint(10, 20, 6))