class Person:

    def display(self, name, age):
        self.name = name
        self.age = age

        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):

    def result(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

        total = m1 + m2 + m3
        print("Total Marks:", total)

        print("Percentage:", total / 3)


# Creating object
obj = Student()

name = input("Enter Student Name: ")
age = int(input("Enter Age: "))

m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))

print("\nStudent Details")

obj.display(name, age)
obj.result(m1, m2, m3)
