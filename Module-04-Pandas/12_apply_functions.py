import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "David", "Priya", "Rahul"],
    "Salary": [50000, 60000, 55000, 65000]
})

print(df)

print("\nApplying a function to increase the salary by 10%:\n")
df["Salary"] = df["Salary"].apply(lambda x: x * 1.10)

print(df)

print("\nUsing a defined function to increase the salary by 10%:\n")
def increase_salary(x):
    return x * 1.10

df["Salary"] = df["Salary"].apply(increase_salary)

print(df)

print("\nUsing apply() with axis=1 to calculate total salary including bonus:\n")
df["Bonus"] = [5000, 6000, 5500, 6500]
df["TotalSalary"] = df.apply(
    lambda row: row["Salary"] + row["Bonus"],
    axis=1
)

print(df)