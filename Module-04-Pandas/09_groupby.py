import pandas as pd

data = {
    "Name": ["John", "David", "Priya", "Rahul", "Anita", "Ravi"],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT", "HR"],
    "Gender": ["Male", "Male", "Female", "Male", "Female", "Male"],
    "Salary": [45000, 60000, 55000, 48000, 62000, 50000]
}

df = pd.DataFrame(data)

print(df)

print("\nGroup by Department\n")
print(df.groupby("Department"))

print("\nTotal Salary by Department\n")
print(df.groupby("Department")["Salary"].sum())

print("\nAverage Salary by Department\n")
print(df.groupby("Department")["Salary"].mean())

print("\nCount of Employees by Department\n")
print(df.groupby("Department")["Name"].count())

print("\nMinimum Salary in Each Department\n")
print(df.groupby("Department")["Salary"].min())

print("\nMaximum Salary in Each Department\n")
print(df.groupby("Department")["Salary"].max())

print("\nAggregated Salary Statistics by Department\n")
print(df.groupby("Department")["Salary"].agg(["sum", "mean", "min", "max", "count"]))

print("\nGroup by Department and Gender\n")
print(df.groupby(["Department", "Gender"])["Salary"].agg(["sum", "mean", "min", "max", "count"]))  