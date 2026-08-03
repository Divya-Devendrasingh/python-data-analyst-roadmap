import pandas as pd

df = pd.read_csv("datasets/employees.csv")

print(df)

print("\nEmployees sorted by Salary\n")
print(df.sort_values("Salary"))

print("\nEmployees sorted by Salary in descending order\n")
print(df.sort_values("Salary", ascending=False))

print("\nEmployees sorted by Department and Salary\n")
print(df.sort_values(["Department", "Salary"]))

print("\nDepartment Ascending, Salary Descending\n")
print(
    df.sort_values(
        ["Department", "Salary"],
        ascending=[True, False]
    )
)

print("\nSorted by Row Index\n")
print(df.sort_index())