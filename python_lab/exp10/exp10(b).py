import matplotlib.pyplot as plt

# Taking user input
n = int(input("Enter number of subjects: "))

subjects = []
marks = []

for i in range(n):
    s = input("Enter subject name: ")
    m = int(input("Enter marks: "))

    subjects.append(s)
    marks.append(m)

# Bar Chart
plt.figure()
plt.bar(subjects, marks)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Line Chart
plt.figure()
plt.plot(subjects, marks, marker='o')
plt.title("Line Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.figure()
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Histogram
plt.figure()
plt.hist(marks, bins=5)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
