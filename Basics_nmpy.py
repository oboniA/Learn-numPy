import numpy as np

a = np.array([1,2,3])
print(a)

b = np.array([[3, 4, 5], [4, 7, 8]])
print(b)

c = np.array([2, 4, 5, 6], dtype='int16')
print(c)

# get dimensions
print("\nDimension of a: ", a.ndim)
print("Dimension of b: ", b.ndim)
print("Dimension of c: ", c.ndim)

# get shape
print("\nShape of a: ", a.shape)
print("Shape of b: ", b.shape)
print("Shape of c: ", c.shape)

# get type
print("\ndata type of a: ", a.dtype)
print("data type of b: ", b.dtype)
print("data type of c: ", c.dtype)

# get size
# sie increases as type increases
print("\nsize of a: ", a.itemsize)
print("size of b: ", b.itemsize)
print("size of c: ", c.itemsize)

# get total size
print("\nTotal size of a: ", a.nbytes)
print("Total size of b: ", b.nbytes)
print("Total size of c: ", c.nbytes)
