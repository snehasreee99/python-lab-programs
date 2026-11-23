
import numpy as np
import pandas as pd

# Taking user input
n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    x = int(input("Enter number: "))
    numbers.append(x)

# NumPy Array
arr = np.array(numbers)

print("\nNumPy Array:")
print(arr)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Pandas Series
s = pd.Series(arr)

print("\nPandas Series:")
print(s)

# Pandas DataFrame
df = pd.DataFrame({
    "Numbers": arr
})

print("\nPandas DataFrame:")
print(df)
