import pandas as pd

df = pd.DataFrame({
    "Employee": ["John", "David", "John", "David", "Priya"],
    "Department": ["HR", "IT", "HR", "IT", "HR"],
    "Sales": [1000, 2000, 1500, 2500, 1800]
})

print(df)

print("\nCreating a pivot table to summarize sales by department:\n")
pivot = pd.pivot_table(
    df,
    index="Department",
    values="Sales",
    aggfunc="sum"
)

print(pivot)

print("\nCreating a pivot table to summarize sales by department with multiple aggregation functions:\n")
pivot_multi = pd.pivot_table(
    df,
    index="Department",
    values="Sales",
    aggfunc=["sum", "mean", "min", "max", "count"]
)

print(pivot_multi)


df = pd.DataFrame({
    "Employee": ["John", "David", "John", "Priya", "Anu"],
    "Department": ["HR", "IT", "HR", "HR", "IT"],
    "Gender": ["Male", "Male", "Male", "Female", "Female"],
    "Sales": [1000, 2000, 1500, 1800, 2200]
})

pivot = pd.pivot_table(
    df,
    index=["Department", "Gender"],
    values="Sales",
    aggfunc="sum"
)

print(pivot)

df = pd.DataFrame({
    "Employee": ["John", "David", "Priya"],
    "Department": ["HR", "IT", "HR"],
    "Gender": ["Male", "Male", "Female"],
    "Sales": [1000, 2000, 1800]
})

pivot = pd.pivot_table(
    df,
    index="Department",
    columns="Gender",
    values="Sales",
    aggfunc="sum"
)

print(pivot)

pivot = pd.pivot_table(
    df,
    index="Department",
    columns="Gender",
    values="Sales",
    aggfunc="sum",
    fill_value=0
)

print(pivot)