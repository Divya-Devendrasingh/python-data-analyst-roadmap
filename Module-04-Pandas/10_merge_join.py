import pandas as pd

employees = pd.DataFrame({
    "EmployeeID": [101,102,103,104,105],
    "Name": ["John","David","Priya","Rahul","Sara"],
    "DepartmentID": [1,2,1,5,2]
})

departments = pd.DataFrame({
    "DepartmentID": [1,2,3,4],
    "Department": ["HR","IT","Finance","Marketing"]
})


print(employees)

print()

print(departments)

print("\n merging the two dataframes on the 'DepartmentID' column")
merged_df = pd.merge(employees, departments, on="DepartmentID")
print(merged_df)

print("\n merging the two dataframes on the 'DepartmentID' column using 'inner' join")

inner_df = pd.merge(
    employees,
    departments,
    on="DepartmentID",
    how="inner"
)
print(inner_df)

print("\n merging the two dataframes on the 'DepartmentID' column using 'left' join")
left_df = pd.merge(
    employees,
    departments,
    on="DepartmentID",
    how="left"
)
print(left_df)

print("\n merging the two dataframes on the 'DepartmentID' column using 'outer' join")
outer_df = pd.merge(
    employees,
    departments,
    on="DepartmentID",
    how="outer"
)
print(outer_df)


employees = pd.DataFrame({
    "EmployeeID": [101,102,103,104],
    "Name": ["John","David","Priya","Rahul"],
    "Department": ["HR","IT","Finance","Marketing"],
    "City": ["New York","San Francisco","Chicago","Los Angeles"]
})
managers = pd.DataFrame({
    "ManagerName": ["Alice","Bob","Charlie","Diana"],
    "Department": ["HR","IT","Finance","Marketing"],
    "City": ["New York","San Francisco","Chicago","Los Angeles"]
})

print("\n merging the two dataframes on the 'Department' and 'City' columns")
merged_df = pd.merge(
    employees,
    managers,
    on=["Department", "City"]
)

print(merged_df)

employees = pd.DataFrame({
    "EmployeeID": [101, 102, 103, 104],
    "Name": ["John", "David", "Priya", "Rahul"],
    "DepartmentID": [1, 2, 1, 5]
})

departments = pd.DataFrame({
    "DepartmentID": [1, 2, 3],
    "Department": ["HR", "IT", "Finance"]
})

merged_df = pd.merge(
                     employees, 
                     departments,
                     on = "DepartmentID"
                 )

print(merged_df)

inner_df = pd.merge(
                    employees,
                    departments,
                    on = "DepartmentID",
                    how = "inner"
                   )

print(inner_df)

left_df = pd.merge(
                    employees,
                    departments,
                    on = "DepartmentID",
                   how = "left"
                   )

print(left_df)

right_df = pd.merge(
                    employees,
                    departments,
                    on = "DepartmentID",
                    how = "right"
                   )

print(right_df)

outer_df = pd.merge(
                  employees,
                  departments,
                  on = "DepartmentID",
                  how = "outer"
                )

print(outer_df)


employees = pd.DataFrame({
    "EmployeeID": [101,102,103],
    "Department": ["HR","IT","HR"],
    "City": ["Hyderabad","Bangalore","Chennai"]
})

managers = pd.DataFrame({
    "Department": ["HR","IT","HR"],
    "City": ["Hyderabad","Bangalore","Chennai"],
    "Manager": ["Ramesh","Suresh","Anita"]
})

merged_df = pd.merge(
                      employees,
                      managers,
                       on = ["Department", "City"]
                     )

print(merged_df)