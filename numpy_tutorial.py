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

# 3-D numpy array
b = np.array([[[1,2], 
               [3, 4]],
              [[5, 6], 
               [7, 8]]])

print(b[0, 1, 1])

# Replace
b[:, 0, :] = [[9, 9], [8, 8]]
print(b)

# Types of arrays
c = np.zeros((2, 3))
print(c)

d = np.ones((2, 3))
print(d)

# Other numbers than 0 or 1
e = np.full((2, 3), 99)
print(e)

# Full like
f = np.full_like(a, 4)
print(f)

# Random decimal numbers
g = np.random.rand(4, 2)
print(g)

# Random interger numbers
h = np.random.randint(4, 8, size=(3, 3))
print(h)

# Identity matrix
i = np.identity(5)
print(i)

# Repeating
j = np.array([[1,2,3]])
r1 = np.repeat(j, 3, axis=0)
print(r1)

# Create test matrix
test = np.ones((5, 5))
test[1:4, 1:4] = 0
test[2,2] = 9
print(test)

# Be careful when copying
# b = a is a shallow copy
k = np.array([1, 2, 3])
l = k.copy()
l[0] = 100
print(k)

# Mathematics
m = np.array([1, 2, 3, 4])
print(f"{m + [1, 0, 1, 0]}")
print(m * 2)
print(np.sin(m))

# Linear Algebra
print("Linear Algebra\n")
m = np.full((2, 3), 1)
n = np.full((3, 2), 2)
print(m)
print(n)

# Matrix multiplication
print(np.matmul(m, n))

# Find the determinant
o = np.identity(5)
print(np.linalg.det(o))


# Statictics
print("Statistics\n")

print(np.min(a, axis=1))
print(np.max(a))
print(np.sum(a, axis=0))

#Reorganizing Arrays

print("Reorganizing Arrays")
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(before)

after = np.reshape(before, (8, 1))
print(after)

# Vertical and Horizonal stacking
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
stacked = np.vstack([v1, v2])
print(stacked)

h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))
stacked = np.hstack((h1, h2))
print(stacked)

# Read from files

file_data = np.genfromtxt('data.txt', delimiter=',')
file_data_int = file_data.astype('int32')
print(file_data_int)
print(file_data_int > 50)
print(file_data_int[file_data_int > 50])

# Can index with a list in numpy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 7]])

print(np.any(file_data_int > 50, axis=0))
print(np.all(file_data_int > 50, axis=0))

# Combining conditionals
combined_conditional = ((file_data_int > 50) & (file_data_int < 100))
print(combined_conditional)

negated_combined_conditional = (~((file_data_int > 50) & (file_data_int < 100)))
print(negated_combined_conditional)