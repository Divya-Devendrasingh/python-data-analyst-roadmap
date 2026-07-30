import numpy as np

sales = np.array([1200, 4500, 800, 6000, 2500])

high_sales = sales[sales > 2000]

print(high_sales)

marks = np.array([85, 42, 76, 38, 91])
failed = marks[marks < 50]
print(failed)

salary = np.array([30000,55000,45000,70000,60000])
bonus = salary[salary >= 50000]
print(bonus)

orders = np.array([101,102,103,104,105,106])
print(orders[orders % 2 == 0])

visitors = np.array([120, 85, 250, 310, 95, 400, 180])
print(visitors[visitors > 200])

sales = np.array([1500,3000,7000,1800,5000])
print(sales[sales > 2500])

marks = np.array([95,45,80,32,67])
print("Failed marks:", marks[marks < 50])

visitors = np.array([120,250,80,340,500,150])
print(visitors[visitors > 200])