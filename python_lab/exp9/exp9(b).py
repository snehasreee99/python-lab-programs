import pandas as pd
import matplotlib.pyplot as plt

months = []
sales = []

n = int(input("Enter number of months: "))

for i in range(n):
    m = input("Enter month name: ")
    s = int(input("Enter sales: "))

    months.append(m)
    sales.append(s)

# Creating DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print("\nSales Data:")
print(df)

# Plotting graph
plt.plot(df["Month"], df["Sales"], marker='o')

plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
