import pandas as pd

# Read CSV file
df = pd.read_csv("datasets/employees.csv")

# Display complete DataFrame
print(df)

# Display first 5 rows
print(df.head())

# Salary greater than 50000
df[df["Salary"] > 50000]

# Salary less than 50000
df[df["Salary"] < 50000]

# Salary greater than or equal to 60000
df[df["Salary"] >= 60000]

# Salary less than or equal to 60000
df[df["Salary"] <= 60000]

# Department is IT
df[df["Department"] == "IT"]

# Salary not equal to 60000
df[df["Salary"] != 60000]

# Multiple conditions
df[(df["Salary"] > 50000) & (df["Department"] == "IT")]

# OR condition
df[(df["Department"] == "HR") | (df["Department"] == "Finance")]

# Using isin() method
df[df["Department"].isin(["HR", "Finance"])]

# Using between() method
df[df["Salary"].between(50000, 70000)]