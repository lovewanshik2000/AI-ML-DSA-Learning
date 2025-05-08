# Learn NumPy
import numpy as np

# 0-D Arrays
zero_arr = np.array(45)
print(zero_arr, type(zero_arr))

# Create NumPy 1-D Array using List
li = [1,2,3,4]
arr = np.array(li)
print(arr, type(arr))

# Create NumPy 1-D Array using Tuple
arr1 = np.array((1, 2, 3, 4, 5))
print(arr1, type(arr1))

# Create NumPy 2-D Array using nested list
arr2 = np.array([1,2,3,4], [4,5,6,7])
print(arr2)