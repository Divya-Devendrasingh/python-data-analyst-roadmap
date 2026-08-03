import pandas as pd

# ---------------------------------------
# Creating a DataFrame
# ---------------------------------------

employee_data = {
    "ID": [101, 102, 103],
    "Name": ["John", "David", "Priya"],
    "Department": ["HR", "IT", "Finance"],
    "Salary": [45000, 60000, 55000]
}

employees = pd.DataFrame(employee_data)

print(employees)

students = {
        "Roll No" : [101, 102, 103],
        "Student" : ["Arun", "Divya", "Kiran"],
        "Marks" : [85, 92, 78]
}

students = pd.DataFrame(students)
print(students)

student_data = {
          "ID" : [101, 102, 103, 104],
          "Name" : ["Arun", "Divya", "Kiran", "Rahul"],
          "Marks" : [85, 92, 78, 88]
            }

students = pd.DataFrame(student_data)
print(students)
print(students.shape)
print(students.size)
print(students.ndim)
print(students.columns)
print(students.index)
print(students.dtypes)

student_data = {
    "ID": [101, 102, 103, 104],
    "Name": ["Arun", "Divya", "Kiran", "Rahul"],
    "Marks": [85, 92, 78, 88]
}

students = pd.DataFrame(student_data)
print(students["Name"])
print(students["Marks"])
print(students[["Name", "Marks"]])

print(students.loc[0])
print(students.loc[2])
print(students.loc[1:2])

print(students.iloc[0])
print(students.iloc[-1])
print(students.iloc[1:3])


student_data = {
    "ID": [101, 102, 103, 104],
    "Name": ["Arun", "Divya", "Kiran", "Rahul"],
    "Marks": [85, 92, 78, 88]
}

students = pd.DataFrame(student_data)

students["Grade"] = ["A", "A", "B", "A"]
print(students)
students["City"] = ["Nellore", "Hyderabad", "Bangalore", "Chennai"]
students["Bonus Marks"] = students["Marks"] + 5
print(students)

students = students.drop(
    ["City", "Bonus Marks"],
    axis=1
)

print(students)