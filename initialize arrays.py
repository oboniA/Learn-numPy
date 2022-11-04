import numpy as np

# ((block, row, column), other_number, data_type)
print("\nAll 0 matrix - 2blocks, with 3row 3 column: ",)
o = np.zeros((2, 3, 3))
print(o)

print("\nAll 1 matrix - 3blocks, with 2row 3 column: ",)
one = np.ones((1, 2, 3))
print(one)

print("\nany other number: ")
other = np.full((2, 2, 2), 88)
print(other)

print("\nany other number with data type: ")
other2 = np.full((2, 2, 2), 88, dtype='float16')
print(other2)

print("\nget an array with given numbers, similar to an existing array: ")
d = np.array([[3, 4, 5], [4, 7, 8]])
sm = np.full_like(d, 1)
print(sm)


