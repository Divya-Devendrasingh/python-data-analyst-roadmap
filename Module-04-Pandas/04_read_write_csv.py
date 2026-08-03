import pandas as pd

# Read CSV file
df = pd.read_csv("datasets/employees.csv")

# Display complete DataFrame
print(df)

# Display first 5 rows
print(df.head())

# Display first 3 rows
print(df.head(3))

# Display last 5 rows
print(df.tail())

# Display last 2 rows
print(df.tail(2))

# Display DataFrame summary
df.info()

# Display statistical summary
print(df.describe())