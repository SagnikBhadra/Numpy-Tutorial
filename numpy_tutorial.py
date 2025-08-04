import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]], dtype="int16")

print("Shapes and Data Types")
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)

print("Size")
print(a.itemsize)
print(a.size)
print(a.nbytes)

# Accessing and Changing Values
print("Accessing and Changing Values")

# Get specific element - [r, c]
print(a[1, 5])

# Get specific row
print(a[1, :])

# Using stepsize [startindex : endindex: stepsize]
print(a[0, 2:6:2])

a[1,5] = 20
print(a)

# Changes Series
a[:, 2] = 5
print(a)