import pandas as pd

data = {
    "Name": ["John", "David", "Priya", "Rahul", "Anita"],
    "Salary": [45000, 60000, None, 48000, 62000],
    "Department": ["IT", None, "HR", "Finance", "IT"]
}

df = pd.DataFrame(data)

print(df)

print("\nMissing Values:\n")
print(df.isnull())

print("\nAvailable Values:\n")
print(df.notnull())

print("\nAfter Removing Missing Values:\n")
print(df.dropna())

print("\nAfter Filling Missing Values:\n")
print(df.fillna(50000))

print("\nAfter Filling Missing Values with Mean:\n")
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

print("\nAfter Filling Missing Values with Median:\n")
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print(df)

print("\nAfter Filling Missing Values with Mode:\n")
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
print(df)