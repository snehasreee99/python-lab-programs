import pandas as pd

# Taking user input
n = int(input("Enter number of students: "))

data = []

for i in range(n):
    name = input("Enter student name: ")

    marks = input("Enter marks (leave blank if missing): ")

    if marks == "":
        marks = None
    else:
        marks = float(marks)

    data.append([name, marks])

# Creating DataFrame
df = pd.DataFrame(data, columns=["Name", "Marks"])

print("\nOriginal Data:")
print(df)

# Checking missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Filling missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Removing duplicate records
df = df.drop_duplicates()

# Exploring data
print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())

print("\nCleaned Data:")
print(df)
