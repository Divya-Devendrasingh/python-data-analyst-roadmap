import pandas as pd

df1 = pd.DataFrame({
    "Name": ["John", "David"],
    "Salary": [50000, 60000]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Rahul"],
    "Salary": [55000, 65000]
})

print(df1)

print()

print(df2)

print("\nConcatenating the two dataframes:\n")
combined_df = pd.concat([df1, df2])

print(combined_df)

print("\nConcatenating the two dataframes with ignore_index=True:\n")
combined_df = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(combined_df)

print("\nConcatenating the two dataframes with keys:\n")
df1 = pd.DataFrame({
    "Name": ["John", "David"]
})

df2 = pd.DataFrame({
    "Salary": [50000, 60000]
})

print(df1)
print()
print(df2)

print("\nConcatenating the two dataframes with axis=1:\n")
combined_df = pd.concat(
    [df1, df2],
    axis=1
)

print(combined_df)

print("\nConcatenating the two dataframes with keys:\n")
df1 = pd.DataFrame({
    "Name": ["John", "David"],
    "Salary": [50000, 60000]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Rahul"],
    "Salary": [55000, 65000]
})

print(df1)
print()
print(df2)

print("\nConcatenating the two dataframes with keys:\n")
combined_df = pd.concat([df1, df2], axis=0)
print(combined_df)

print("\nConcatenating the two dataframes with keys and ignore_index=True:\n")
combined_df = pd.concat([df1, df2], axis=0, ignore_index=True)
print(combined_df)

print("\nConcatenating the two dataframes with keys and axis=1:\n")
combined_df = pd.concat([df1, df2], axis=1)
print(combined_df)