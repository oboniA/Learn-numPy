import numpy as np

"""
get this shape 
 [1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]
"""

arr = np.ones((5, 5))
print(arr)

z = np.zeros((3, 3))
print(z)

z[1, 1] = 9
print(z)

# merging two arrays
arr[1:-1, 1:-1] = z           # shows range selection
print(arr)



