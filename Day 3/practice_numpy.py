#----------------- NumPy ------------------- #

import numpy as np

# Python list copies the list 
python_list = [1, 2, 3, 4]
python_list *= 2

print(python_list)

# NumPy list multiplies each element by 2
numpy_list = np.array([1, 2, 3, 4])
numpy_list *= 2

print(numpy_list)

#----- Multidimensional array --------#
array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F'],
                  ['G', 'H', 'I']])
print(array.shape)

# Chain indexing
print(array[0][0])

# Multidimensional indexing (faster than chain indexing)
print(array[0, 0])

word = array[0, 0] +  array[1, 0] + array[2, 1] + array[1, 0]

print(word)
print()

#------- Slicing --------#
slice_array = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]])

# array[start:end:step]
print(slice_array[0:3])
print()
print(slice_array[1:4])
print()
print(slice_array[1:2:4])
print()
print(slice_array[:, -1])
print()
print(slice_array[:, 0:3])
print()
print(slice_array[:, ::-1])
print()
print(slice_array[2:4, 0:2]) # print(slice_array[2:, 0:2]) works the same 
print() 

#--------- Arithmetic ---------#

# Scalar Arithmetic
ary  = np.array([1, 2, 3])
print(ary + 1) 
print(ary - 2)
print(ary * 3)
print(ary / 4)
print(ary ** 5)
print()

# Vectorized math functions
vector_ary = np.array([1.01, 2.5, 3.99])
print(np.sqrt(vector_ary))
print(np.round(vector_ary))
# Always round down
print(np.floor(vector_ary))
# Always round up
print(np.ceil(vector_ary))

radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)
print()

# Element-wise arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# Comparison operators 
scores = np.array([91, 55, 100, 73, 82, 64])
print(scores == 100)
print(scores >= 60)
print(scores < 60)
scores[scores < 60] = 0
print(scores)