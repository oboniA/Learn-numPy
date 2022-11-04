import numpy as np

data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
b = data
print("given the data:\n", b)

print("\n0th block, 0th row, 0th column:")
print(b[0, 0, 0])

print("\n1st block, 0th row, 1st column:")
print(b[1, 0, 1])

print("\n1st row of both blocks:")
print(b[:,1,:])

print("\nreplace 1st row of both blocks with 0s:")
b[:,1,:] = [[0, 0], [0, 0]]
print(b)





