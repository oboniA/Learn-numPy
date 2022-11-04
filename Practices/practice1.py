import numpy as np

"""
get this shape 
 [1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 9. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]
"""

a = np.identity(5)
print(a)

a[0, :] = [1, 1, 1, 1, 1]
print(a)

a[: ,0] = [1, 1, 1, 1, 1]
print(a)

a[4, :] = [1, 1, 1, 1, 1]
print(a)

a[: ,4] = [1, 1, 1, 1, 1]
print(a)

a[1, 1] = 0
print(a)

a[2, 2] = 9
print(a)

a[3, 3] = 0
print(a)



