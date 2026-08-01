import pandas as pd

print("=" * 50)
print("PANDAS SERIES")
print("=" * 50)

# ---------------------------------------
# Creating a Series
# ---------------------------------------

marks = pd.Series([85, 90, 78, 92, 88])

print("\nStudent Marks:")
print(marks)

x = pd.Series([10, 20, 30, 40])
print(x)

marks = pd.Series([85, 90, 78])
print(marks)

cities = pd.Series(["Delhi", "Mumbai", "Chennai", "Hyderabad"])
print(cities)

marks = pd.Series([85, 90, 78, 92, 88])

print(marks[0])
print(marks[2])
print(marks[:3])
print(marks[1:4])
print(marks.iloc[-1])

# ---------------------------------------
# Series Attributes
# ---------------------------------------

marks = pd.Series([85, 90, 78, 92, 88])

print("Index:", marks.index)
print("Values:", marks.values)
print("Data Type:", marks.dtype)
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Dimensions:", marks.ndim)

marks = pd.Series([95, 80, 75, 88]) 
print(marks.size) 
print(marks.ndim) 
print(marks.shape) 
print(marks.values) 
print(marks.index)

# ---------------------------------------
# Custom Index
# ---------------------------------------

salary = pd.Series(
    [45000, 52000, 61000],
    index=["John", "David", "Priya"]
)

print("salary:", salary)
print(salary["David"])

cities = pd.Series(
    ["Delhi", "Mumbai", "Hyderabad"],
    index=["D", "M", "H"]
)

print(cities)

products = pd.Series([25000, 1200, 800],
                      index = ["Laptop", "Keyboard", "Mouse"])
print(products)
print(products["Keyboard"])

Students = pd.Series([85, 92, 78],
                     index = ["Arun", "Divya", "Kiran"])
print(Students)
print(Students["Divya"])

fruits = pd.Series(
    [120, 80, 150],
    index=["Apple", "Banana", "Orange"]
)
print(fruits["Banana"])
print(fruits.index)


# ---------------------------------------
# Creating Series from Dictionary
# ---------------------------------------

student_marks = {
    "Arun": 85,
    "Divya": 92,
    "Kiran": 78
}

marks = pd.Series(student_marks)
print(marks)

prices = {
    "Laptop": 55000,
    "Mouse": 1200,
    "Keyboard": 2500
}

product_prices = pd.Series(prices)
print(product_prices)

items = {
    "Rice": 65,
    "Sugar": 45,
    "Oil": 160
}

products = pd.Series(items)
print(products)

marks = {
          "Math" : 95,
          "Science" : 88,
          "English" : 91
           }

sub_marks = pd.Series(marks)
print(sub_marks)
print(sub_marks["Science"])