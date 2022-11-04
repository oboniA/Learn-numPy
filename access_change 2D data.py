import numpy as np

data = np.array([[3, 6, 5, 8, 11], [4, 7, 10, 12, 14], [4, 6, 8, 1, 0]])
a = data
print("Print the data:\n",a)

# get specific element
print("\n0th row, 3rd column:")
print(a[0, 3])

print("\n1st row, 2nd column:")
print(a[1, 2])

# get specific column
print("\n2nd column:")
print(a[:, 2])

# get specific row
print("\n0th row:")
print(a[0, :])

# row, start_index:end_index:step_size
print("\n1st row, from index1 to index4, every second element:")
print(a[1, 1:4:2])

print("\n1st row, from index1 to last index, every second element:")
print(a[1, 1:-1:2])

# replace a value in the matrix
print("\nreplace the second element of 1st row with 11:")
a[1, 2] = 11
print(a)

# change entire column to given digit
print("\nChange the entire 2nd column to 0:")
a[:, 2] = 0      # all zero
print(a)

print("\nreplace the element in 2nd column with 1, 2, respectively")
a[:,2] = [1,2,3]
print(a)










