import pandas as pd

df = pd.read_csv("datasets/employees.csv")

print(df.columns)

print(df.index)

print(df.shape)

print(df["Name"])

print(df["Salary"])

print(df[["Name", "Salary"]])

print(df[["Department", "Salary"]])