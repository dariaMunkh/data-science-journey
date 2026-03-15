import numpy as np

#-------------- Filtering -------------------#
# Filtering =  Refers to the process of selecting elements
#              from an array that match a given condition 

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors  = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds)
print()

# Retain the original shape of the array
# Fill value replaces anything that does not match the condition 
adults1 = np.where(ages >= 18, ages, 0)
print(adults1)
print()

#------------------ Random Numbers -----------------#
# Setting a seed allows to reproduce the same value again
rng = np.random.default_rng(seed = 1)

print(rng.integers(low = 1, high = 101, size = (3, 2)))
print()

# Random floating numbers 
print(np.random.uniform(low = -1, high = 1, size = 3))
print()

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)
print()

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruit = rng.choice(fruits, size = 3)
print(fruit)
print()