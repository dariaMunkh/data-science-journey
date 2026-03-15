import numpy as np

#------------------ Broadcasting -----------------#
# Broadcasting allows NumPy to perform operations on arrays 
# with different shapes by virtually expanding dimensions 
# so they match the larger array's shape.

# The dimensions have the same size.
# OR 
# One of the dimensions has a size of 1

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

#----------------- Aggregate Functions ---------------#
# Aggregate functions = summarize data and typically
#                       return a single value

ary = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])

# Sum of all the elements in ary
print(np.sum(ary))

# Mean of all the elements in ary
print(np.mean(ary))

# Standard deviation of all the elements in ary
print(np.std(ary))

# Variance of all the elements in ary
print(np.var(ary))

# Minimum value of all the elements in ary
print(np.min(ary))

# Maximum value of all the elements in ary
print(np.max(ary))

# Position of the min value of all the elements in ary
print(np.argmin(ary))

# Position of the max value of all the elements in ary
print(np.argmax(ary))

# Sum of all columns
print(np.sum(ary, axis = 0))

# Sum of all rows
print(np.sum(ary, axis = 1))