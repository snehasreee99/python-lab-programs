# Creating a dictionary

student = {}

student["id"] = int(input("Enter Student ID: "))
student["name"] = input("Enter Student Name: ")
student["course"] = input("Enter Course: ")
student["marks"] = int(input("Enter Marks: "))

print("\nStudent Dictionary:")
print(student)

# Display keys
print("\nKeys:", student.keys())

# Display values
print("Values:", student.values())

# Display items
print("Items:", student.items())

# Access value using get()
print("Student Name:", student.get("name"))

# Update dictionary
student.update({"marks": 90})
print("Updated Dictionary:", student)

# Remove an item
student.pop("course")
print("After Removing Course:", student)

# Display length
print("Length:", len(student))
